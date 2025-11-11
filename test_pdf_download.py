import os
import time
import streamlit as st
import re

# --- Configuration ---
REPORTS_DIR = "reports"
os.makedirs(REPORTS_DIR, exist_ok=True)


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


# Sample compliance report markdown for testing
SAMPLE_REPORT = """# Foundation Compliance Report

## Executive Summary

This report analyzes the RCC structural drawings for compliance with **IS 456:2000** and **SP 34**.

## Project Information

- **Project Name**: Sample Foundation Project
- **Location**: Mangalore, Karnataka
- **Date**: 2024
- **Analysis Date**: """ + time.strftime("%Y-%m-%d") + """

## Compliance Analysis

### 1. Foundation Design

The foundation design has been reviewed against IS 456:2000 requirements:

- ✅ Minimum cover requirements are met
- ✅ Reinforcement detailing follows SP 34 guidelines
- ⚠️ Some dimensions need verification

### 2. Missing or Wrong Information

The following information requires attention:

1. **Site Conditions**: Site-specific conditions need to be specified
2. **Environmental Exposure**: Exposure class should be clearly defined
3. **Load Combinations**: All load combinations should be documented

### 3. Recommendations

1. Provide site-specific geotechnical data
2. Clarify environmental exposure conditions
3. Document all design load cases

## Conclusion

The foundation design generally complies with IS 456:2000, but additional information is required for complete verification.

---

*This is a sample report for testing PDF download functionality.*
"""

# Streamlit UI
st.set_page_config(
    page_title="PDF Download Test",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 PDF Download Test")
st.markdown("Test the PDF download functionality with sample data")

st.header("📋 Sample Compliance Report")
st.markdown("---")

# Display the sample report
st.markdown(SAMPLE_REPORT)

# Download buttons
st.markdown("---")
st.header("📥 Download Options")

col1, col2 = st.columns(2)

with col1:
    # Download as Markdown
    st.subheader("Markdown Download")
    st.download_button(
        label="📥 Download Report as Markdown",
        data=SAMPLE_REPORT,
        file_name=f"test_compliance_report_{int(time.time())}.md",
        mime="text/markdown"
    )

with col2:
    # Download as PDF
    st.subheader("PDF Download")
    timestamp = int(time.time())
    pdf_filename = f"test_compliance_report_{timestamp}.pdf"
    pdf_path = os.path.join(REPORTS_DIR, pdf_filename)
    
    # Try to convert to PDF
    try:
        pdf_success, error_msg = markdown_to_pdf(SAMPLE_REPORT, pdf_path)
        if pdf_success and os.path.exists(pdf_path):
            with open(pdf_path, "rb") as pdf_file:
                st.download_button(
                    label="📄 Download Report as PDF",
                    data=pdf_file.read(),
                    file_name=pdf_filename,
                    mime="application/pdf"
                )
            st.success("✅ PDF generated successfully!")
        else:
            if error_msg:
                st.warning(f"⚠️ {error_msg}")
            else:
                st.info("💡 PDF conversion requires 'weasyprint' or 'reportlab'. Install with: `pip install weasyprint` or `pip install reportlab`")
    except Exception as e:
        st.error(f"❌ PDF conversion error: {e}")

# Additional info
st.markdown("---")
st.info("💡 This is a test page. Use this to verify PDF download functionality without making API calls.")

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This test page allows you to:
    - Test PDF download functionality
    - Verify markdown to PDF conversion
    - Check if weasyprint or reportlab is working
    
    **No API calls required!**
    """)
    
    st.header("📝 Instructions")
    st.markdown("""
    1. Review the sample report above
    2. Click download buttons to test
    3. Check if PDF generation works
    4. Install missing libraries if needed
    """)

