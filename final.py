import os
import time
import streamlit as st
import re
from llm_handler import analyze_rcc_drawing
from prompt import INITIAL_EXTRACTION_PROMPT, REFINEMENT_PROMPT_TEMPLATE
from embedding_service import embedding_model
from vector_db import VectorStore
from llm_service import generate_compliance_report

# --- Configuration ---
REPORTS_DIR = "reports"
UPLOADS_DIR = "uploads"
FIRST_EXTRACT_DIR = "first_extract"
RESULT_DIR = "RESULT"
os.makedirs(REPORTS_DIR, exist_ok=True)
os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(FIRST_EXTRACT_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

# Initialize vector DB (assuming it's already populated)
vectordb = VectorStore(collection_name="is_codes_docs", folder_path="./chroma_db")

def markdown_to_pdf(markdown_text: str, output_path: str):
    """
    Converts markdown text to PDF using markdown + weasyprint.
    Falls back to reportlab if weasyprint fails (better Windows support).
    Returns (success: bool, error_message: str or None)
    """
    # Try WeasyPrint first
    try:
        import markdown
        from weasyprint import HTML
        from weasyprint.text.fonts import FontConfiguration
        
        # Convert markdown to HTML
        html_content = markdown.markdown(markdown_text, extensions=['tables', 'fenced_code'])
        
        # Create full HTML document
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    line-height: 1.6;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 4px;
                    border-radius: 3px;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Generate PDF
        font_config = FontConfiguration()
        HTML(string=full_html).write_pdf(output_path, font_config=font_config)
        return True, None
    except ImportError:
        # WeasyPrint not installed, try reportlab
        pass
    except Exception as e:
        # WeasyPrint installed but failed (e.g., GTK libraries missing on Windows)
        error_msg = str(e)
        if 'libgobject' in error_msg.lower() or 'gtk' in error_msg.lower() or 'cannot load library' in error_msg.lower():
            # Try fallback with reportlab (better Windows support)
            pass
        else:
            # Other WeasyPrint errors - try reportlab anyway
            pass
    
    # Try fallback with reportlab (better Windows support)
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        import html
        
        # Convert markdown to HTML-like format for reportlab
        text = markdown_text
        # Simple markdown to HTML conversion for reportlab
        text = re.sub(r'^#+\s+(.+)$', r'<b>\1</b>', text, flags=re.MULTILINE)
        text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
        text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
        text = re.sub(r'`(.+?)`', r'<font name="Courier">\1</font>', text)
        
        # Create PDF
        doc = SimpleDocTemplate(output_path, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        
        # Custom style for better formatting
        custom_style = ParagraphStyle(
            'Custom',
            parent=styles['Normal'],
            fontSize=11,
            leading=14,
            spaceAfter=12,
        )
        
        # Split text into paragraphs and add to PDF
        for line in text.split('\n'):
            if line.strip():
                # Escape HTML special characters but preserve our formatting tags
                # First, temporarily replace our tags
                line = line.replace('<b>', '___BOLD_START___').replace('</b>', '___BOLD_END___')
                line = line.replace('<i>', '___ITALIC_START___').replace('</i>', '___ITALIC_END___')
                line = line.replace('<font name="Courier">', '___CODE_START___').replace('</font>', '___CODE_END___')
                # Escape HTML
                line = html.escape(line)
                # Restore our tags
                line = line.replace('___BOLD_START___', '<b>').replace('___BOLD_END___', '</b>')
                line = line.replace('___ITALIC_START___', '<i>').replace('___ITALIC_END___', '</i>')
                line = line.replace('___CODE_START___', '<font name="Courier">').replace('___CODE_END___', '</font>')
                story.append(Paragraph(line, custom_style))
            else:
                story.append(Spacer(1, 0.2*inch))
        
        doc.build(story)
        return True, None
    except ImportError:
        return False, "PDF conversion requires either 'weasyprint' or 'reportlab'. Install with: `pip install weasyprint` or `pip install reportlab`"
    except Exception as e:
        return False, f"PDF conversion failed with reportlab: {str(e)}"
    
    # If we get here, both methods failed
    return False, "PDF conversion requires either 'weasyprint' (with GTK+ libraries) or 'reportlab'. For Windows, install reportlab: `pip install reportlab`"


# Streamlit UI
st.set_page_config(
    page_title="Foundation compliance check using AI",
    page_icon="🧑‍🔬",
    layout="wide"
)

st.title("🧑‍🔬 Foundation compliance check using AI")
st.markdown("Analyze RCC structural drawings for compliance with IS 456:2000 and SP 34")

# Initialize session state
if 'initial_report' not in st.session_state:
    st.session_state.initial_report = None
if 'final_report' not in st.session_state:
    st.session_state.final_report = None
if 'pdf_filename' not in st.session_state:
    st.session_state.pdf_filename = None

# Section 1: PDF Upload and Initial Report Generation
st.header("📄 Step 1: Upload PDF and Generate Initial Report")

uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type=['pdf'],
    help="Upload an RCC structural drawing PDF for analysis"
)

if uploaded_file is not None:
    # Save uploaded file
    pdf_path = os.path.join(UPLOADS_DIR, uploaded_file.name)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.session_state.pdf_filename = uploaded_file.name
    st.success(f"✅ File uploaded: {uploaded_file.name}")

    # Generate initial report button
    if st.button("🔍 Generate Initial Report", type="primary"):
        with st.spinner("Analyzing PDF and generating initial compliance report..."):
            try:
                initial_report = analyze_rcc_drawing(pdf_path, INITIAL_EXTRACTION_PROMPT)
                st.session_state.initial_report = initial_report
                
                # Save the initial report
                timestamp = int(time.time())
                initial_filename = f"initial_report_{os.path.basename(uploaded_file.name)}_{timestamp}.md"
                initial_filepath = os.path.join(FIRST_EXTRACT_DIR, initial_filename)
                with open(initial_filepath, 'w', encoding='utf-8') as f:
                    f.write(initial_report)
                
                st.success("✅ Initial report generated successfully!")
            except Exception as e:
                st.error(f"❌ Error during analysis: {e}")

# Display Full Initial Report
if st.session_state.initial_report:
    st.header("📋 Step 2: Initial Compliance Report")
    st.markdown("---")
    print(st.session_state.initial_report)
    st.markdown(st.session_state.initial_report)
    st.markdown("---")
    init_col1, init_col2 = st.columns(2)

    with init_col1:
        initial_md_filename = f"initial_compliance_report_{int(time.time())}.md"
        st.download_button(
            label="📥 Download Initial Report as Markdown",
            data=st.session_state.initial_report,
            file_name=initial_md_filename,
            mime="text/markdown"
        )

    with init_col2:
        initial_pdf_filename = f"initial_compliance_report_{int(time.time())}.pdf"
        initial_pdf_path = os.path.join(REPORTS_DIR, initial_pdf_filename)

        try:
            pdf_success, error_msg = markdown_to_pdf(st.session_state.initial_report, initial_pdf_path)
            if pdf_success and os.path.exists(initial_pdf_path):
                with open(initial_pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label="📄 Download Initial Report as PDF",
                        data=pdf_file.read(),
                        file_name=initial_pdf_filename,
                        mime="application/pdf"
                    )
            else:
                if error_msg:
                    st.info(f"💡 {error_msg}")
                else:
                    st.info("💡 PDF conversion requires 'weasyprint' or 'reportlab'. Install with: `pip install weasyprint` or `pip install reportlab`")
        except Exception as e:
            st.info(f"💡 PDF conversion not available. Error: {e}")
    
    # Section 3: User Input
    st.header("✏️ Step 3: Provide Additional Information")
    st.markdown("Please provide any missing information or corrections:")
    
    user_provided_info = st.text_area(
        "User Input",
        height=150,
        placeholder="Example:\nsite - mangalore, karnataka\nsevere condition to be taken\ntake limiting value for rest missing information",
        help="Enter any additional information that addresses the missing or wrong information items"
    )
    
    # Section 4: Generate Final Report
    if st.button("🚀 Generate Final Report", type="primary"):
        if not user_provided_info.strip():
            st.warning("⚠️ Please provide additional information before generating the final report.")
        else:
            with st.spinner("Generating final compliance report with RAG-enhanced analysis..."):
                try:
                    refinement_prompt = REFINEMENT_PROMPT_TEMPLATE.format(
                        previous_analysis=st.session_state.initial_report,
                        user_input=user_provided_info
                    )
                    
                    final_report = generate_compliance_report(
                        vectordb=vectordb,
                        embedding_model=embedding_model,
                        Initial_report=refinement_prompt,
                        previous_analysis=st.session_state.initial_report,
                        user_input=user_provided_info,
                    )
                    
                    st.session_state.final_report = final_report
                    
                    # Save final report to RESULT folder
                    timestamp = int(time.time())
                    final_filename = f"final_report_{os.path.basename(uploaded_file.name)}_{timestamp}.md"
                    final_filepath = os.path.join(RESULT_DIR, final_filename)
                    with open(final_filepath, 'w', encoding='utf-8') as f:
                        f.write(final_report)
                    
                    st.success(f"✅ Final report generated and saved to {final_filepath}!")
                except Exception as e:
                    st.error(f"❌ Error generating final report: {e}")

# Display Final Report
if st.session_state.final_report:
    st.header("📊 Step 4: Final Compliance Report")
    st.markdown("---")
    
    # Display the report
    st.markdown(st.session_state.final_report)
    
    # Download button
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        # Download as Markdown
        st.download_button(
            label="📥 Download Final Report as Markdown",
            data=st.session_state.final_report,
            file_name=f"compliance_report_{int(time.time())}.md",
            mime="text/markdown"
        )
    
    with col2:
        # Download as PDF
        timestamp = int(time.time())
        pdf_filename = f"compliance_report_{timestamp}.pdf"
        pdf_path = os.path.join(REPORTS_DIR, pdf_filename)
        
        # Try to convert to PDF
        try:
            pdf_success, error_msg = markdown_to_pdf(st.session_state.final_report, pdf_path)
            if pdf_success and os.path.exists(pdf_path):
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label="📄 Download Final Report as PDF",
                        data=pdf_file.read(),
                        file_name=pdf_filename,
                        mime="application/pdf"
                    )
            else:
                if error_msg:
                    st.info(f"💡 {error_msg}")
                else:
                    st.info("💡 PDF conversion requires 'weasyprint' or 'reportlab'. Install with: `pip install weasyprint` or `pip install reportlab`")
        except Exception as e:
            st.info(f"💡 PDF conversion not available. Error: {e}")

# Sidebar information
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This tool analyzes RCC structural drawings for compliance with:
    - **IS 456:2000** (Plain & Reinforced Concrete)
    - **SP 34** (Handbook on Concrete Reinforcement Detailing)
    """)
    
    st.header("📝 Instructions")
    st.markdown("""
    1. Upload your PDF drawing
    2. Generate initial report
    3. Review missing information
    4. Provide additional details
    5. Generate final report
    6. Download the report
    """)
    
    if st.session_state.initial_report:
        st.success("✅ Initial report generated")
    if st.session_state.final_report:
        st.success("✅ Final report generated")

