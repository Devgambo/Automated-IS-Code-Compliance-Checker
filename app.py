import os
import time
import argparse # Import the argparse library
from llm_handler import analyze_rcc_drawing
from prompts import INITIAL_EXTRACTION_PROMPT

REPORTS_DIR = "reports"
UPLOADS_DIR = "uploads"

def ensure_dirs():
    """Ensure that the reports and uploads directories exist."""
    os.makedirs(REPORTS_DIR, exist_ok=True)
    os.makedirs(UPLOADS_DIR, exist_ok=True)

def save_report(content, filename):
    """Saves the report content to a file."""
    filepath = os.path.join(REPORTS_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Report saved to {filepath}")
    return filepath

def get_pdf_path(filename):
    """Constructs the full path to the PDF file and checks for its existence."""
    if not filename:
        print("Error: No PDF filename provided.")
        return None

    pdf_path = os.path.join(UPLOADS_DIR, filename)
    
    if not os.path.exists(pdf_path):
        print(f"Error: The file '{filename}' was not found in the '{UPLOADS_DIR}/' directory.")
        return None
        
    print(f"Found PDF file: {pdf_path}")
    return pdf_path

def main():
    """Main function to run the RCC design compliance check."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="RCC Design Compliance Check AI")
    parser.add_argument("filename", type=str, help="The name of the PDF file in the 'uploads' directory to analyze.")
    args = parser.parse_args()

    ensure_dirs()
    print("--- RCC Design Compliance Check AI ---")
    print("Note: Please make sure you have created a .env file with your GEMINI_API_KEY.")

    pdf_path = get_pdf_path(args.filename)
    if not pdf_path:
        return

    print("\nStarting initial analysis...")
    try:
        initial_report = analyze_rcc_drawing(pdf_path, INITIAL_EXTRACTION_PROMPT)
    except Exception as e:
        print(f"\nAn error occurred during the initial analysis: {e}")
        return
        
    print("\nInitial analysis complete.")
    print("\n--- INITIAL REPORT ---")
    print(initial_report)
    
    timestamp = int(time.time())
    save_report(initial_report, f"initial_report_{timestamp}.md")
    print("\nCompliance check process finished.")

if __name__ == "__main__":
    main()
