# WO-380: Automated IS Code Compliance Checker for Structural Design Drawings

## 🚀 Project Overview

An AI-powered system that automates compliance checking for structural design drawings (PDFs). The system parses RCC (Reinforced Cement Concrete) foundation drawings, extracts key parameters using computer vision, and generates comprehensive compliance reports aligned with Indian Standards (IS 456:2000 and SP 34:1987).

### Key Capabilities

- **PDF to Image Conversion**: Converts structural design PDFs to high-quality images at 200 DPI
- **AI-Powered Analysis**: Uses Google Gemini Vision AI (via OpenRouter) to extract structural information
- **Comprehensive Data Extraction**: Extracts dimensions, reinforcement details, material specifications, and compliance parameters
- **Automated Report Generation**: Creates detailed markdown reports with extracted data and compliance status
- **RAG-Enhanced Analysis**: Retrieval-Augmented Generation (RAG) system for accurate IS code clause citations
- **Vector Database Integration**: ChromaDB for semantic search of IS code provisions

---

## ✨ Features

- **Vision-Assisted Analysis**: Google Gemini 2.5 Flash vision model for drawing interpretation
- **PDF Processing**: PyMuPDF for high-quality PDF to image conversion
- **Vector Database**: ChromaDB with sentence-transformers embeddings for code provision retrieval
- **CLI Workflow**: Simple command-line interface for batch processing
- **Comprehensive Extraction**: 22+ compliance criteria extraction including:
  - Concrete and reinforcement grades
  - Cover requirements and development lengths
  - Foundation specifications
  - Seismic zone considerations
  - Detailing requirements
- **Professional Reports**: Markdown reports with timestamped versions

---

## 📋 Prerequisites

- **Python 3.10+** (Python 3.11 recommended)
- **Git** (for cloning the repository)
- **Internet access** (for AI API calls)
- **API Key**: OpenRouter API key for Gemini Vision access

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd WO-380
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root directory:

```bash
# Required: OpenRouter API Key for Gemini Vision
OPENROUTER_API_KEY=your_openrouter_api_key_here

# Optional: For direct Gemini API access (if needed)
GEMINI_API_KEY=your_gemini_api_key_here
```

#### Getting API Keys

- **OpenRouter API Key**: Visit [OpenRouter](https://openrouter.ai/) to create an account and get your API key
- **Gemini API Key** (optional): Visit [Google AI Studio](https://makersuite.google.com/app/apikey) for direct Gemini access

---

## 🚀 Quick Start

### Basic Usage

1. **Place your PDF file** in the `uploads/` directory:
   ```bash
   # Ensure the uploads directory exists
   mkdir -p uploads
   
   # Copy your PDF file
   cp your_drawing.pdf uploads/
   ```

2. **Run the analysis**:
   ```bash
   python app.py your_drawing.pdf
   ```

3. **View the report**: The system will:
   - Convert PDF to images
   - Analyze using Gemini Vision AI
   - Generate a comprehensive compliance report
   - Save results to `reports/initial_report_<timestamp>.md`

### Example Output

```bash
--- RCC Design Compliance Check AI ---
Note: Please make sure you have created a .env file with your OPENROUTER_API_KEY.
Found PDF file: uploads/7.pdf

Starting initial analysis...
Initial analysis complete.

--- INITIAL REPORT ---
[Comprehensive markdown report with compliance checklist]

Report saved to reports/initial_report_1234567890.md
Compliance check process finished.
```

---

## 📖 Detailed Usage Guide

### Command-Line Interface

The main entry point is `app.py`, which provides a simple CLI:

```bash
python app.py <filename>
```

**Arguments:**
- `filename`: The name of the PDF file in the `uploads/` directory (e.g., `7.pdf`)

**What it does:**
1. Validates the PDF file exists in `uploads/`
2. Converts PDF pages to high-resolution images (200 DPI)
3. Sends images to Gemini Vision AI for analysis
4. Extracts compliance-relevant information
5. Generates a structured markdown report
6. Saves the report with a timestamp

### Programmatic Usage

You can also use the modules directly in your Python code:

```python
from llm_handler import analyze_rcc_drawing
from prompt import INITIAL_EXTRACTION_PROMPT

# Analyze a PDF
pdf_path = "uploads/your_drawing.pdf"
report = analyze_rcc_drawing(pdf_path, INITIAL_EXTRACTION_PROMPT)
print(report)
```

### PDF to Image Conversion

```python
from pdf_to_image import pdf_to_image

# Convert a specific page to image
image_path = pdf_to_image(
    pdf_path="uploads/drawing.pdf",
    output_image="output.jpg",
    page_number=1,  # Page to convert (1-indexed)
    zoom=2  # Zoom factor for quality
)
```

### Using Vector Database for Code Retrieval

```python
from vector_db import VectorDB
from embedding_service import generate_embedding

# Initialize vector database
db = VectorDB()

# Generate embedding for query
query = "What are the cover requirements for foundations?"
embedding = generate_embedding(query)

# Search for relevant code provisions
results = db.query(embedding, top_k=5)
```

---

## 📊 Understanding the Output

### Generated Files

1. **Markdown Report**: Comprehensive extraction report with timestamp
   - Location: `reports/initial_report_<timestamp>.md`
   - Format: GitHub-flavored markdown with tables and structured sections

### Report Structure

The generated report includes:

- **Document Type Verification**: Confirms if the drawing is a foundation drawing
- **Site Location**: Extracted or flagged as missing
- **Code Standards**: References to IS 456:2000 and SP 34:1987
- **NOTES Section**: Verification of presence and completeness
- **Compliance Checklist**: 22+ criteria with status indicators:
  - ✅ Compliant
  - ❌ Non-Compliant
  - ⚠️ Missing Information
  - ❓ Cannot Verify
  - ➖ Not Applicable
- **Extracted Values**: All dimensions, specifications, and annotations
- **Summary Statistics**: Compliance percentage and breakdown

### Example Report Sections

```markdown
## Compliance Checklist

| Criterion | Extracted Value | Code Requirement | Status | Notes |
|-----------|----------------|------------------|--------|-------|
| Concrete Grade | M25 | M20 minimum | ✅ Compliant | - |
| Reinforcement Grade | Fe415 | Fe415/Fe500 | ✅ Compliant | - |
| Clear Cover | 50mm | 40mm minimum | ✅ Compliant | - |
```

---

## 🧩 Key Modules

### Core Modules

- **`app.py`**: CLI entrypoint; orchestrates extraction and saves reports
- **`llm_handler.py`**: High-level LLM workflow for RCC drawing analysis
  - `analyze_rcc_drawing()`: Main function for PDF analysis
  - `pdf_to_images()`: PDF to PIL Image conversion
  - `analyze_rcc_drawing_from_images()`: Vision API integration
- **`llm_service.py`**: LLM service helpers and report refinement
- **`gemini_vision.py`**: Gemini Vision integration utilities
- **`pdf_to_image.py`**: PDF to image conversion utilities
- **`vector_db.py`**: ChromaDB vector store integration
- **`embedding_service.py`**: Embedding generation using sentence-transformers
- **`prompt.py`**: Prompt templates for extraction and analysis
- **`data_loader.py`**: Data loading utilities for vector database

### Supporting Files

- **`requirements.txt`**: Python package dependencies
- **`METHODOLOGY.md`**: Detailed technical methodology and architecture
- **`DOCKER_SETUP.md`**: Docker development environment setup

---

## 📁 Project Structure

```
WO-380/
├── app.py                      # CLI entrypoint
├── llm_handler.py              # Main LLM workflow
├── llm_service.py              # LLM service helpers
├── gemini_vision.py            # Gemini Vision integration
├── embedding_service.py        # Embeddings generation
├── vector_db.py               # ChromaDB integration
├── pdf_to_image.py            # PDF/image utilities
├── prompt.py                   # Prompt templates
├── data_loader.py              # Data loading utilities
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── METHODOLOGY.md              # Technical documentation
├── DOCKER_SETUP.md            # Docker setup guide
├── .env                        # API keys (create this)
│
├── uploads/                    # Place PDFs here
├── reports/                    # Generated markdown reports
├── chroma_db/                  # Vector DB data (auto-created)
├── convertedimages/            # Generated images (auto-created)
├── SP34_md/                    # SP 34 code documents
└── sample_pdfs/               # Sample test PDFs
```

> **Note**: Large/binary/data folders (`uploads/`, `reports/`, `chroma_db/`, `convertedimages/`) are ignored by git via `.gitignore`.

---

## 🐳 Docker Setup (Optional)

The project includes Docker support for a consistent development environment. See `DOCKER_SETUP.md` for detailed instructions.

### Quick Docker Commands

```bash
# Build the Docker image
docker compose build

# Start the development environment
docker compose up -d

# Access the container shell
docker exec -it python-dev-env bash

# Inside container: install dependencies and run
pip install -r requirements.txt
python app.py 7.pdf
```

---

## 🐛 Troubleshooting

### Common Issues

1. **"File not found" Error**
   - Ensure the PDF is in the `uploads/` directory
   - Check that the filename matches exactly (case-sensitive)
   - Verify the file extension is `.pdf`

2. **"OPENROUTER_API_KEY not found"**
   - Create a `.env` file in the project root
   - Add `OPENROUTER_API_KEY=your_key_here`
   - Ensure the key is valid and has sufficient credits

3. **"Error converting PDF to image"**
   - Check if the PDF is password-protected
   - Verify the PDF is not corrupted
   - Ensure PyMuPDF is installed correctly

4. **"ChromaDB errors"**
   - Delete and re-create `chroma_db/` directory if the index is corrupted
   - Ensure write permissions in the project directory

5. **Poor extraction results**
   - Use higher quality PDFs with clear text/drawings
   - Ensure drawings follow standard engineering notation
   - Check that the NOTES section is clearly visible

6. **Import errors**
   - Ensure virtual environment is activated
   - Run `pip install -r requirements.txt` again
   - Check Python version (3.10+ required)

### Getting Help

1. Check the generated image files in `convertedimages/` to verify PDF conversion
2. Review console output for specific error messages
3. Verify all dependencies are installed: `pip list`
4. Ensure API keys are valid and have sufficient credits
5. Check `METHODOLOGY.md` for detailed technical information

---

## 🔧 Advanced Configuration

### Environment Variables

```bash
# Required
OPENROUTER_API_KEY=your_openrouter_api_key

# Optional
GEMINI_API_KEY=your_gemini_api_key  # For direct Gemini access
```

### Customizing Image Conversion

In `pdf_to_image.py`, you can adjust:
- **Page number**: Which page to convert (default: 1)
- **Zoom factor**: Image quality (higher = better quality, larger file)
- **Output format**: JPG, PNG, etc.

### Customizing Prompts

Edit `prompt.py` to customize extraction criteria:
- `INITIAL_EXTRACTION_PROMPT`: Main extraction prompt
- `prompt1`: Alternative detailed extraction prompt
- `REFINEMENT_PROMPT_TEMPLATE`: Report refinement prompt

### Vector Database Configuration

The vector database uses:
- **Embedding Model**: `all-MiniLM-L6-v2` (384 dimensions)
- **Database**: ChromaDB with persistent storage
- **Retrieval**: Top 5 most relevant provisions by cosine similarity

---

## 🧪 Development

### Running Tests

```bash
# Test environment setup
python test_env.py

# Test PDF download/processing
python test_pdf_download.py
```

### Jupyter Notebooks

The project includes Jupyter notebooks for exploration:
- `main.ipynb`: Main exploration notebook
- `FINAL.ipynb`: Final analysis notebook

To use Jupyter:
```bash
# Install Jupyter (if not already installed)
pip install jupyter jupyterlab

# Start Jupyter Lab
jupyter lab
```

### Code Structure

The codebase follows a modular architecture:
- **Input Processing**: PDF conversion and image preprocessing
- **Vision Analysis**: AI-powered drawing interpretation
- **Data Extraction**: Structured information extraction
- **RAG Enhancement**: Code provision retrieval and citation
- **Report Generation**: Markdown report creation

---

## 📚 Documentation

- **`README.md`**: This file - quick start and usage guide
- **`METHODOLOGY.md`**: Comprehensive technical documentation including:
  - System architecture
  - RAG implementation details
  - AI model specifications
  - Workflow diagrams
  - Compliance criteria details

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes with clear commits
4. Add/update documentation where relevant
5. Test thoroughly
6. Submit a pull request

---

## 📄 License

[Add your license information here]

---

## 🙏 Acknowledgments

- **Google Gemini Vision AI** for image analysis capabilities
- **OpenRouter** for unified AI API access
- **IS 456:2000** and **SP 34:1987** code provisions for compliance checking
- **ChromaDB** and **sentence-transformers** for vector search capabilities
- The civil engineering community for domain expertise

---

## 🔮 Future Enhancements

- Support for additional Indian Standards (IS 1893, IS 13920)
- Web interface using Streamlit
- Batch processing for multiple drawings
- Interactive report refinement
- 3D drawing support
- Handwritten text recognition
- Multi-language support

---

**Ready to automate your structural design compliance checks?** 

Run `python app.py <your-file.pdf>` and get your first report in minutes! 🚀
