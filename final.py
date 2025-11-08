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
os.makedirs(REPORTS_DIR, exist_ok=True)
os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(FIRST_EXTRACT_DIR, exist_ok=True)

# Initialize vector DB (assuming it's already populated)
vectordb = VectorStore(collection_name="is_codes_docs", folder_path="./chroma_db")


def extract_missing_info_section(report_text: str) -> str:
    """
    Extracts the "## Missing or Wrong Information" section from the report.
    Returns the section if found, otherwise returns a message.
    """
    # Pattern to find the section (handles variations in formatting)
    patterns = [
        r'##\s*Missing or Wrong Information.*?(?=##\s|\*\*|📚|📌|## UPDATED|## ✅|## 📄|\Z)',
        r'##\s*Missing.*?Wrong.*?Information.*?(?=##|\Z)',
        r'\*\*Missing or Wrong Information\*\*.*?(?=##|\Z)',
        r'Missing or Wrong Information.*?(?=##|\Z)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, report_text, re.DOTALL | re.IGNORECASE)
        if match:
            section = match.group(0).strip()
            # Remove any trailing section headers that might have been captured
            section = re.sub(r'\n##\s+[A-Z].*$', '', section, flags=re.DOTALL)
            return section
    
    return "## Missing or Wrong Information\n\n*Section not found in the report. Please check the full report below.*"


def markdown_to_pdf(markdown_text: str, output_path: str):
    """
    Converts markdown text to PDF using markdown + weasyprint.
    Falls back to saving as .md if PDF conversion fails.
    """
    try:
        import markdown
        from weasyprint import HTML, CSS
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
        return True
    except ImportError:
        # If weasyprint is not available, save as markdown
        with open(output_path.replace('.pdf', '.md'), 'w', encoding='utf-8') as f:
            f.write(markdown_text)
        return False
    except Exception as e:
        st.error(f"Error converting to PDF: {e}")
        # Fallback: save as markdown
        with open(output_path.replace('.pdf', '.md'), 'w', encoding='utf-8') as f:
            f.write(markdown_text)
        return False


# Streamlit UI
st.set_page_config(
    page_title="RCC Drawing Compliance Checker",
    page_icon="🏗️",
    layout="wide"
)

st.title("🏗️ RCC Drawing Compliance Checker")
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
                st.balloons()
            except Exception as e:
                st.error(f"❌ Error during analysis: {e}")

# Display Full Initial Report
if st.session_state.initial_report:
    st.header("📋 Step 2: Initial Compliance Report")
    st.markdown("---")
    st.markdown(st.session_state.initial_report)
    
    # Also show Missing or Wrong Information section separately
    st.header("📋 Step 3: Missing or Wrong Information")
    st.markdown("Review the items that need attention:")
    
    missing_info = extract_missing_info_section(st.session_state.initial_report)
    st.markdown(missing_info)
    
    # Section 4: User Input
    st.header("✏️ Step 4: Provide Additional Information")
    st.markdown("Please provide any missing information or corrections:")
    
    user_provided_info = st.text_area(
        "User Input",
        height=150,
        placeholder="Example:\nsite - mangalore, karnataka\nsevere condition to be taken\ntake limiting value for rest missing information",
        help="Enter any additional information that addresses the missing or wrong information items"
    )
    
    # Section 5: Generate Final Report
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
                    
                    # Save final report
                    timestamp = int(time.time())
                    final_filename = f"final_report_{os.path.basename(uploaded_file.name)}_{timestamp}.md"
                    final_filepath = os.path.join(REPORTS_DIR, final_filename)
                    with open(final_filepath, 'w', encoding='utf-8') as f:
                        f.write(final_report)
                    
                    st.success("✅ Final report generated successfully!")
                    st.balloons()
                except Exception as e:
                    st.error(f"❌ Error generating final report: {e}")

# Display Final Report
if st.session_state.final_report:
    st.header("📊 Step 5: Final Compliance Report")
    st.markdown("---")
    
    # Display the report
    st.markdown(st.session_state.final_report)
    
    # Download button
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        # Download as Markdown
        st.download_button(
            label="📥 Download Report as Markdown",
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
            pdf_success = markdown_to_pdf(st.session_state.final_report, pdf_path)
            if pdf_success and os.path.exists(pdf_path):
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label="📄 Download Report as PDF",
                        data=pdf_file.read(),
                        file_name=pdf_filename,
                        mime="application/pdf"
                    )
            else:
                st.info("💡 PDF conversion requires 'weasyprint'. Install it with: `pip install weasyprint`")
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

