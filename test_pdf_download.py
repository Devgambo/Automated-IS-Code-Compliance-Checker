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
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.lib import colors
        import html
        
        # Create PDF
        doc = SimpleDocTemplate(output_path, pagesize=letter, 
                               rightMargin=72, leftMargin=72,
                               topMargin=72, bottomMargin=18)
        styles = getSampleStyleSheet()
        story = []
        
        # Define custom styles
        h1_style = ParagraphStyle(
            'H1',
            parent=styles['Heading1'],
            fontSize=14,
            textColor=colors.HexColor('#1a1a1a'),
            spaceAfter=8,
            spaceBefore=8,
        )
        
        h2_style = ParagraphStyle(
            'H2',
            parent=styles['Heading2'],
            fontSize=12,
            textColor=colors.HexColor('#2a2a2a'),
            spaceAfter=6,
            spaceBefore=6,
        )
        
        h3_style = ParagraphStyle(
            'H3',
            parent=styles['Heading3'],
            fontSize=11,
            textColor=colors.HexColor('#3a3a3a'),
            spaceAfter=5,
            spaceBefore=5,
        )
        
        normal_style = ParagraphStyle(
            'Normal',
            parent=styles['Normal'],
            fontSize=9,
            leading=11,
            spaceAfter=4,
        )
        
        # Helper function to convert markdown inline formatting to reportlab XML
        def convert_inline_formatting(text):
            # Escape HTML first
            text = html.escape(text)
            # Convert markdown to reportlab XML
            # Bold: **text** or __text__ (process before italic to avoid conflicts)
            text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
            text = re.sub(r'__(.+?)__', r'<b>\1</b>', text)
            # Code: `text` (process before italic)
            text = re.sub(r'`(.+?)`', r'<font name="Courier" color="darkblue">\1</font>', text)
            # Italic: *text* (single asterisk, not double)
            # Match *text* but not **text** (already processed)
            text = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<i>\1</i>', text)
            # Italic: _text_ (single underscore, not double)
            text = re.sub(r'(?<!_)_([^_]+?)_(?!_)', r'<i>\1</i>', text)
            return text
        
        # Helper function to parse markdown table
        def parse_table(lines, start_idx):
            """Parse a markdown table starting at start_idx. Returns (table_data, end_idx)"""
            table_data = []
            i = start_idx
            
            # Read header
            if i >= len(lines) or not lines[i].strip().startswith('|'):
                return None, start_idx
            
            header_line = lines[i].strip()
            if not header_line.startswith('|') or not header_line.endswith('|'):
                return None, start_idx
            
            headers = [cell.strip() for cell in header_line.split('|')[1:-1]]
            i += 1
            
            # Skip separator row (|---|---|)
            if i < len(lines) and re.match(r'^\|[\s\-:]+$', lines[i].strip()):
                i += 1
            
            # Read data rows
            while i < len(lines):
                row_line = lines[i].strip()
                if not row_line.startswith('|'):
                    break
                
                cells = [cell.strip() for cell in row_line.split('|')[1:-1]]
                if len(cells) == len(headers):
                    table_data.append(cells)
                i += 1
            
            if table_data:
                return [headers] + table_data, i
            return None, start_idx
        
        # Parse markdown line by line
        lines = markdown_text.split('\n')
        i = 0
        in_list = False
        list_items = []
        
        while i < len(lines):
            line = lines[i].rstrip()
            
            # Empty line
            if not line.strip():
                if in_list and list_items:
                    # Add list items
                    for item in list_items:
                        bullet_text = convert_inline_formatting(item)
                        story.append(Paragraph(f"• {bullet_text}", normal_style))
                    list_items = []
                    in_list = False
                story.append(Spacer(1, 0.1*inch))
                i += 1
                continue
            
            # Tables (check before headers to avoid conflicts)
            if line.strip().startswith('|') and '|' in line[1:]:
                table_data, new_idx = parse_table(lines, i)
                if table_data:
                    # Create table
                    table_style = TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f0f0f0')),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#000000')),
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (-1, 0), 8),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                        ('TOPPADDING', (0, 0), (-1, 0), 8),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                        ('FONTSIZE', (0, 1), (-1, -1), 8),
                        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                        ('LEFTPADDING', (0, 0), (-1, -1), 4),
                        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                        ('TOPPADDING', (0, 1), (-1, -1), 5),
                        ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
                    ])
                    
                    # Convert table data to Paragraphs with formatting
                    formatted_table_data = []
                    for row_idx, row in enumerate(table_data):
                        formatted_row = []
                        for cell in row:
                            formatted_cell = Paragraph(convert_inline_formatting(cell), normal_style)
                            formatted_row.append(formatted_cell)
                        formatted_table_data.append(formatted_row)
                    
                    # Create table with auto column widths
                    # Calculate available width (page width minus margins)
                    available_width = letter[0] - 144  # 72*2 for left and right margins
                    col_widths = [available_width / len(table_data[0])] * len(table_data[0])
                    pdf_table = Table(formatted_table_data, colWidths=col_widths)
                    pdf_table.setStyle(table_style)
                    story.append(pdf_table)
                    story.append(Spacer(1, 0.15*inch))
                    i = new_idx
                    continue
            
            # Headers
            if line.startswith('#'):
                if in_list and list_items:
                    for item in list_items:
                        bullet_text = convert_inline_formatting(item)
                        story.append(Paragraph(f"• {bullet_text}", normal_style))
                    list_items = []
                    in_list = False
                
                if line.startswith('###'):
                    header_text = convert_inline_formatting(line[3:].strip())
                    story.append(Paragraph(header_text, h3_style))
                elif line.startswith('##'):
                    header_text = convert_inline_formatting(line[2:].strip())
                    story.append(Paragraph(header_text, h2_style))
                elif line.startswith('#'):
                    header_text = convert_inline_formatting(line[1:].strip())
                    story.append(Paragraph(header_text, h1_style))
                i += 1
                continue
            
            # Horizontal rule
            if re.match(r'^---+$|^===+$|^\*\*\*+$', line):
                story.append(Spacer(1, 0.15*inch))
                story.append(Paragraph('<para alignment="center">' + '─' * 50 + '</para>', normal_style))
                story.append(Spacer(1, 0.15*inch))
                i += 1
                continue
            
            # Unordered list
            if re.match(r'^[-*+]\s+', line):
                in_list = True
                item_text = re.sub(r'^[-*+]\s+', '', line)
                list_items.append(item_text)
                i += 1
                continue
            
            # Ordered list
            if re.match(r'^\d+\.\s+', line):
                if in_list and list_items:
                    for item in list_items:
                        bullet_text = convert_inline_formatting(item)
                        story.append(Paragraph(f"• {bullet_text}", normal_style))
                    list_items = []
                    in_list = False
                item_text = re.sub(r'^\d+\.\s+', '', line)
                item_text = convert_inline_formatting(item_text)
                story.append(Paragraph(item_text, normal_style))
                i += 1
                continue
            
            # Regular paragraph
            if in_list and list_items:
                for item in list_items:
                    bullet_text = convert_inline_formatting(item)
                    story.append(Paragraph(f"• {bullet_text}", normal_style))
                list_items = []
                in_list = False
            
            # Convert inline formatting and add paragraph
            formatted_text = convert_inline_formatting(line)
            story.append(Paragraph(formatted_text, normal_style))
            i += 1
        
        # Handle any remaining list items
        if in_list and list_items:
            for item in list_items:
                bullet_text = convert_inline_formatting(item)
                story.append(Paragraph(f"• {bullet_text}", normal_style))
        
        doc.build(story)
        return True, None
    except ImportError:
        return False, "PDF conversion requires either 'weasyprint' or 'reportlab'. Install with: `pip install weasyprint` or `pip install reportlab`"
    except Exception as e:
        return False, f"PDF conversion failed with reportlab: {str(e)}"
    
    # If we get here, both methods failed
    return False, "PDF conversion requires either 'weasyprint' (with GTK+ libraries) or 'reportlab'. For Windows, install reportlab: `pip install reportlab`"


# Sample compliance report markdown for testing
SAMPLE_REPORT = """Okay, I will analyze the provided RCC structural drawing PDF for "FOUNDATIONS" and check its compliance against IS 456:2000 and SP 34, following your step-by-step process.

---

### Step 0: Initial Document Check

- **0.1: Verify if the document is an RCC structural drawing of "FOUNDATIONS" only.**
    - The drawing is titled "FOUNDATION PLAN AND DETAILS" and clearly shows foundation layouts, footing schedules, column-to-footing connections, and typical footing sections. It does not display beams, slabs, or other superstructure elements in detail.
    - **Status: Compliant (It is a foundation drawing).**

- **0.2: Find the site location.**
    - The client is "D.K.Z.P HIGHER PRIMARY SCHOOL AT BOLLYARU". Bollyaru appears to be the site location.
    - **Extracted Value: Bollyaru.**
    - **Status: Compliant.**

- **0.3: Confirm compliance checks are based only on IS 456:2000 and SP 34.**
    - Confirmed.

### Step 1: Locate the "NOTES" Section

- The "NOTES" section is clearly present on the drawing, separate from "GENERAL NOTES".
- **Status: Compliant.**

### Step 2 & 3: Extract and Verify Design Parameters from "NOTES"

Here's the detailed checklist and compliance report:

| Criteria | Extracted Value | Compliance Check | Status |
|---|---|---|---|
| **1. Grade of Concrete** | M25 for all R.C.C. works. | M25 is a common grade suitable for many environmental conditions. Compliance cannot be fully verified without specific environmental exposure class for Bollyaru, but M25 generally meets requirements for 'moderate' exposure. | **Compliant (Assuming Moderate Exposure)** |
| **2. Reinforcement Bars** | Type: HYSD TMT Bars, Grade: Fe 500, Conforming to IS 1786-1985. Vertical reinforcement details provided for columns (e.g., C1: 4Y16(d)+2Y12, C2: 6Y16(d)+6Y12, C3: 4Y20(e)+8Y16). Footing reinforcement (Bottom) mentioned as Y10@175, Y10@125, Y10@100. Ties also mentioned (Y8@200, Y8@400). | Fe 500 is standard and compliant. Specific diameters and spacing for shear reinforcement (ties) are provided. | **Compliant** |
| **3. Lap Length** | 50 times dia of the bar, to be staggered such that not more than 50% of the bars are lapped at a section. | Compliant with minimum recommendation of 50d. Staggering also mentioned. | **Compliant** |
| **4. Clear Cover** | Footing/Wall: 50 mm, Columns: 40 mm, Slab: 20 mm, Beam: 25 mm. | Footing cover of 50mm is provided. IS 456:2000 specifies a minimum of 50mm for footings. If PCC is not specified, a higher clear cover (70-75mm) is often assumed. The drawing explicitly shows PCC under the footing in "SECTION X". Column cover of 40mm is compliant. Slab and beam covers are also compliant with standard practices for those elements (though not directly part of foundation design notes in this context). | **Compliant (for Footing/Column; PCC is specified in Section X)** |
| **5. Development Length (Ld)** | 50 times the dia of the bar. | Compliant with common practice and SP 34 considerations. | **Compliant** |
| **6. Safe Bearing Capacity (SBC) of soil** | 21 T/m² | SBC is mentioned. PCC is explicitly shown in "Typical Plan of Footing" and "Section X". | **Compliant** |
| **7. Seismic Zone and Wind Load** | Not mentioned. | This information is crucial for structural design, especially in India, and is mandatory. | **Missing Information** |
| **8. Building Limitations** | Structure is designed for Ground + 1 storey only. | Limitation explicitly stated. | **Compliant** |
| **9. Structure's Purpose** | Higher Primary School at Bollyaru. | Purpose is mentioned. | **Compliant** |
| **10. Floor Heights** | Plinth Beam, First Floor, Terrace Lvl, but no specific floor heights (e.g., in meters). | Relative levels are indicated, but exact floor to floor heights are missing. | **Missing Information** |
| **11. Schedule of Footings** | "SCHEDULE OF FOOTINGS" table is present and consistent with the "FOUNDATION LAYOUT". | Table is present and seems consistent. | **Compliant** |
| **12. Footing Type** | Isolated footings (F1, F2, F3, F4) are used. | Isolated footings are appropriate for a Ground + 1 storey building. | **Compliant** |
| **13. Reinforcement in High-Rise Buildings** | The building is specified as Ground + 1 storey, which is not considered high-rise. Thus, this check is not directly applicable. | Not Applicable (Building is not high-rise). | **Not Applicable** |
| **14. Raft Foundation Reinforcement** | Raft foundation is not used. Isolated footings are used. | Not Applicable. | **Not Applicable** |
| **15. Lift Design** | A lift is not shown or mentioned in the drawing. | No lift design implies no lift pit. | **Not Applicable (No lift designed)** |
| **16. Soil Improvement** | Not mentioned. | No information on soil improvement. | **Missing Information** |
| **17. Column Ties** | Ties for columns C1, C2, C3 are shown for "FOUNDATION TO FIRST FLOOR LVL." and "FIRST FLOOR TO TERRACE LVL.", implying continuity. The schematics show closed ties. | Ties are generally shown as continuous within column segments. | **Compliant** |
| **18. Plan of Ties** | No separate plan for ties. Tie details are shown within the column mark details. | While detailed in columnar sections, a separate plan is ideal for clarity, especially in complex layouts. | **Missing Information (Separate plan)** |
| **19. Outer Ties Check** | Column ties are specified (e.g., Y8@200 and Y8@400). Percentage of steel in columns for C1, C2, C3: C1 (4x16+2x12), C2 (6x16+6x12), C3 (4x20+8x16). For a 300x300 column, assuming C1 (4x16 + 2x12) is ~1.2% (Area_steel = 4*201 + 2*113 = 1030 mm^2, Area_gross = 300*300 = 90000 mm^2, % = 1.14%). Similarly for other columns, the percentage appears to be > 0.8%. Footing reinforcement (Y10@175) for F1 with 300 depth (0.12%) - area of steel = 78.5 mm^2/175mm * 1000mm = 448 mm^2. Area of concrete = 1000mm*300mm = 300000 mm^2. Percentage = 0.149%. This meets the 0.12% minimum. | Column steel percentage appears to be compliant (>0.8%). Footing steel percentage also appears compliant (>0.12%). Tie specifications are present. | **Compliant** |
| **20. Cross-Section Area** | Not explicitly stated in the notes whether gross cross-section area is used for columns/footings and effective area for slabs. However, typical design practice implies this. | Implicitly standard practice, but not explicitly stated. | **Missing Information (Explicit statement)** |
| **21. Steel Curtailment** | No explicit statement about curtailment of steel in upper floors. However, the design is for Ground + 1 storey, where significant curtailment might not be as critical or as variable as in multi-storey buildings. The column reinforcement shown is for "FOUNDATION TO FIRST FLOOR LVL" and "FIRST FLOOR TO TERRACE LVL", and it appears identical for some columns (e.g., C1) or adjusted (e.g., C2, C3). This implies some level of design consideration for different stories. | Not explicitly stated as "curtailment" but different reinforcement for different levels implies consideration. Given G+1, a 50% reduction might not be expected. | **Implicitly considered, but not explicitly stated as "curtailment".** |
| **22. Maximum Steel Percentage in Columns** | Max steel percentage is not explicitly stated in notes. Based on calculations in point 19, the percentages for C1, C2, C3 are around 1.14% to 2.2% (e.g., C2 (6x16+6x12) for 300x300 column: Area_steel = 6*201 + 6*113 = 1884 mm^2. % = 1884/90000 = 2.09%). This is well below the 6% (or 4% with lapping) limit as per IS 456:2000. | Though not stated, the calculated percentages are compliant. | **Compliant (Based on calculated percentage)** |

### Step 5: Report Missing or Wrong Information

The following items were flagged as "Missing Information" or "Missing or Wrong Information":

1.  **Seismic Zone and Wind Load:** This information is mandatory for structural design in India as per IS codes and is not provided in the notes.
2.  **Floor Heights:** While relative levels are shown, specific floor-to-floor heights (e.g., in meters) are not mentioned.
3.  **Soil Improvement:** No details regarding any soil improvement methods used at the site are mentioned.
4.  **Plan of Ties:** A separate, comprehensive plan for column ties is not present. Details are embedded within column section drawings, which can be less clear for complex tie arrangements.
5.  **Cross-Section Area (Explicit Statement):** It is not explicitly stated whether gross cross-section area is used for columns/footings and effective area for slabs for design calculations, though this is implied by standard practice.

---

**Summary of Compliance:**

Out of 18 applicable checklist items (excluding "Not Applicable" items), 13 are compliant, and 5 have missing information. This means 72% of the conditions are satisfied. Since more than 50% of the conditions are satisfied, this appears to be a valid foundation drawing.

**Final Verdict:** This document is a valid RCC structural drawing for "FOUNDATIONS" and generally complies with the analyzed IS 456:2000 and SP 34 requirements, but it has some missing information that should be clarified for a complete design.
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

