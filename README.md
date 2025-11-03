# WO-380: Automated IS Code Compliance Checker for Structural Design Drawings


## 🚀 Project Overview

Automate compliance checks for structural design drawings (PDFs). The system parses drawings, extracts key parameters, and generates AI-assisted reports aligned with Indian Standards (e.g., IS 456, IS 1786, IS 13920).

---

## 🔍 What This System Does

- **Uploads structural design PDFs** into `WO-380/uploads/`
- **Extracts** dimensions, reinforcement details, grades, and annotations
- **Generates markdown reports** under `WO-380/reports/`

---

## ✨ Features

<<<<<<< HEAD
- **PDF to Image Conversion**: Converts structural design PDFs to high-quality images
- **AI-Powered Analysis**: Uses Google Gemini Vision AI to extract structural information
- **Comprehensive Data Extraction**: Extracts dimensions, reinforcement details, material specifications, and more
- **Automated Report Generation**: Creates detailed markdown reports with extracted data
- **Multiple AI Models Support**: Supports Gemini, Groq, and Qwen Vision models
- **IS 456:2000 Compliance Checker**: Comprehensive RCC structure compliance verification
- **SP 34:1987 Detailing Checker**: Reinforcement detailing and anchorage compliance
=======
- **Gemini Vision-assisted analysis** via `gemini_vision.py`
- **PDF tools** using `PyMuPDF` and `pdfplumber`
- **Vector DB** with `chromadb` for semantic retrieval
- **Embeddings** via `sentence-transformers`
- **CLI workflow** driven by `WO-380/app.py`
>>>>>>> complete

## 📋 Prerequisites

- Python 3.10+
- Git
- Internet access for AI API calls

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd WO-380
```

### 2. Create virtual environment

```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r WO-380/requirements.txt
```

### 4. Environment variables

<<<<<<< HEAD
Create a `.env` file in the project root:

```bash
# For Gemini Vision AI
GEMINI_API_KEY=your_gemini_api_key_here

# For Groq Vision AI (optional)
GROQ_API_KEY=your_groq_api_key_here

# For Qwen Vision AI (optional)
QWEN_API_KEY=your_qwen_api_key_here
```

#### Getting API Keys:

- **Gemini API Key**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey) to get your API key
- **Groq API Key**: Visit [Groq AI](https://console.groq.com/) to get your API key
- **Qwen API Key**: Visit [Qwen AI](https://dashscope.console.aliyun.com/) to get your API key

## 🚀 Quick Start

### Basic Usage

1. **Place your PDF file** in the project directory
2. **Update the file name** in `main.py` (line 12):
   ```python
   pdf_path = "your_drawing.pdf"  # Change to your PDF filename
   ```
3. **Run the main script**:
   ```bash
   python main.py
   ```

### Example Output

The script will:
- Convert your PDF to an image
- Analyze it using Gemini Vision AI
- Generate a comprehensive report
- Save results to a timestamped markdown file

## 📖 Detailed Usage Guide

### 1. Using the Main Script (`main.py`)

The main script provides a complete workflow:

```python
# Edit these lines in main.py
pdf_path = "1st floor Slab details.pdf"  # Your PDF file
image_path = "1st floor Slab details.jpg"  # Output image name
```

**What it does:**
- Converts PDF to high-resolution image
- Extracts structural data using AI
- Generates detailed compliance report
- Saves results to markdown file

### 2. Using Individual Components

#### PDF to Image Conversion

```python
from pdf_to_image import pdf_to_image

# Convert PDF to image
image_path = pdf_to_image(
    pdf_path="your_drawing.pdf",
    output_path="output.jpg",
    page_number=1,  # Page to convert
    zoom=2  # Zoom factor for quality
)
```

#### AI Analysis with Different Models

**Gemini Vision:**
```python
from gemini_vision import analyse_image
from prompt import prompt1

result = analyse_image("your_image.jpg", prompt1)
print(result)
```

**Groq Vision:**
```python
from groq_vision import analyse_image
from prompt import prompt1

result = analyse_image("your_image.jpg", prompt1)
print(result)
```

**Qwen Vision:**
```python
from qwen_vision import analyse_image
from prompt import prompt1

result = analyse_image("your_image.jpg", prompt1)
print(result)
```

### 3. Customizing the Analysis

#### Modifying the Prompt

Edit `prompt.py` to customize what information to extract:

```python
prompt1 = """
Extract the following information from this structural drawing:
- Drawing title and number
- Dimensions and measurements
- Reinforcement details
- Material specifications
- Any compliance-related information
"""
```

#### Adding New AI Models

1. Create a new file (e.g., `new_model_vision.py`)
2. Implement the `analyse_image(image_path, prompt)` function
3. Update `main.py` to use your new model

### 4. Using Compliance Checkers

#### IS 456:2000 Compliance Checker

```python
from IS_456_2000 import DesignChecker, Material, Dimensions, Loads, Reinforcement, MemberType, ExposureCondition

# Create a design checker
checker = DesignChecker()

# Define your structure
material = Material(fck=25, fy=415)
dimensions = Dimensions(length=5000, width=300, depth=500, effective_depth=450, cover=25)
loads = Loads(dead_load=15, live_load=10)
reinforcement = Reinforcement(main_steel_area=1256, main_bar_dia=20)

# Check compliance
results = checker.check_compliance(
    member_type=MemberType.BEAM,
    dimensions=dimensions,
    material=material,
    loads=loads,
    exposure=ExposureCondition.MODERATE,
    reinforcement=reinforcement
)

# Generate report
report = checker.generate_compliance_report(results)
print(report)
```

#### SP 34:1987 Detailing Checker

```python
from SP_34 import DetailingChecker, MemberGeometry, ReinforcementBar, SteelGrade, ConcreteGrade

# Create a detailing checker
checker = DetailingChecker()

# Define member geometry and reinforcement
geometry = MemberGeometry(length=5000, width=300, depth=500, effective_depth=450, cover=25)
reinforcement = [
    ReinforcementBar(diameter=20, number=4, spacing=150, length=5000, position="bottom"),
    ReinforcementBar(diameter=12, number=2, spacing=200, length=5000, position="top")
]

# Check detailing compliance
results = checker.check_beam_detailing(
    geometry=geometry,
    reinforcement=reinforcement,
    steel_grade=SteelGrade.FE415,
    concrete_grade=ConcreteGrade.M25
)

# Generate detailed report
report = checker.generate_detailing_report(results)
print(report)
```

## 📊 Understanding the Output

### Generated Files

1. **Image File**: High-resolution JPG version of your PDF
2. **Markdown Report**: Comprehensive extraction report with timestamp

### Report Structure

The generated report includes:
- **General Information**: Date, drawing details
- **Drawing Information**: Title, number, revision, scale
- **Personnel & Consultants**: Client, structural consultant details
- **Grid System & Dimensions**: All measurements and spacings
- **Slab Specifications**: Thickness, reinforcement details
- **Beam Details**: Dimensions and reinforcement schedules
- **Material Specifications**: Concrete and steel grades
- **Cover & Development Requirements**: Clear cover specifications
- **Summary Table**: All numeric data in organized format

### Example Report Sections

```
**Slab Specifications**
- Slab Thickness: 5" (127 mm)
- Distribution Reinforcement: Y8 @ 10" c/c (254 mm)
- General Slab Reinforcement: Y8 @ 7" c/c (178 mm)

**Beam Details**
- Beam FB20: 9" x 18" (229 mm x 457 mm)
- Top Reinforcement: 3Y12
- Bottom Reinforcement: 2Y16
```

## 🔧 Advanced Configuration

### Environment Variables
=======
Create a `.env` at the repo root (ignored by git):
>>>>>>> complete

```bash
# Required
GEMINI_API_KEY=your_gemini_api_key_here

<<<<<<< HEAD
# Optional - for other AI models
GROQ_API_KEY=your_groq_key
QWEN_API_KEY=your_qwen_key
CONVERTAPI_SECRET=your_convertapi_secret
```

### Customizing Image Conversion

In `pdf_to_image.py`, you can adjust:
- **Page number**: Which page to convert
- **Zoom factor**: Image quality (higher = better quality, larger file)
- **Output format**: JPG, PNG, etc.

### Error Handling

The script includes comprehensive error handling:
- Missing PDF files
- Invalid API keys
- Network connectivity issues
- Image conversion failures

## 🐛 Troubleshooting

### Common Issues

1. **"PDF file not found"**
   - Ensure your PDF file is in the project directory
   - Check the filename in `main.py` matches exactly

2. **"GEMINI_API_KEY not found"**
   - Create a `.env` file with your API key
   - Ensure the key is valid and has sufficient credits

3. **"Error converting PDF to image"**
   - Check if the PDF is password-protected
   - Ensure the PDF is not corrupted
   - Try a different page number

4. **Poor extraction results**
   - Use higher zoom factor for better image quality
   - Ensure the PDF has clear, readable text/drawings
   - Try different AI models for comparison

### Getting Help

1. Check the generated image file to verify PDF conversion
2. Review the console output for specific error messages
3. Ensure all dependencies are installed correctly
4. Verify your API keys are valid and have sufficient credits

## 📁 Project Structure

```
WO-380/
├── main.py                 # Main execution script
├── pdf_to_image.py        # PDF to image conversion
├── gemini_vision.py       # Gemini Vision AI integration
├── groq_vision.py         # Groq Vision AI integration
├── qwen_vision.py         # Qwen Vision AI integration
├── prompt.py              # AI analysis prompts
├── IS 456_2000.py         # IS 456:2000 compliance checker
├── IS 456_2000.txt        # IS 456:2000 code text
├── SP_34.py              # SP 34:1987 detailing checker
├── SP_34.txt             # SP 34:1987 code text
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .env                  # API keys (create this)
└── extracted_data_*.md   # Generated reports
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 🙏 Acknowledgments

- Google Gemini Vision AI for image analysis capabilities
- ConvertAPI for PDF to image conversion
- IS 456:2000 and SP 34:1987 code provisions for compliance checking
- The civil engineering community for domain expertise
=======
# Optional
CONVERTAPI_SECRET=your_convertapi_secret
```

> Get a Gemini API key from Google AI Studio: `https://makersuite.google.com/app/apikey`
>>>>>>> complete

---

## 🚀 Quick Start (CLI)

1. Place your PDF in `WO-380/uploads/` (e.g., `7.pdf`).
2. Run the analyzer from the repo root:

```bash
python WO-380/app.py 7.pdf
```

Output:
- A timestamped markdown report in `WO-380/reports/`, e.g., `initial_report_1760....md`.
- Console printout of the initial report.

---

## 🧩 Key Modules

- `WO-380/app.py`: CLI entrypoint; orchestrates extraction and saves reports
- `WO-380/llm_handler.py`: High-level LLM workflow for RCC drawing analysis
- `WO-380/gemini_vision.py`: Gemini Vision integration helpers
- `WO-380/pdf_to_image.py`: PDF → image conversion utilities
- `WO-380/vector_db.py`: ChromaDB vector store integration
- `WO-380/embedding_service.py`: Embedding generation utilities
- `WO-380/prompt.py`: Prompt templates for extraction

---

## 🧪 Notebooks

- `WO-380/main.ipynb`, `WO-380/demo.ipynb`: Explore extraction steps and iterate on prompts.

---

## 🐳 Run with Docker (optional)

The included compose file provides a dev container with Python and ports for future services/notebooks.

```bash
docker compose up -d
docker exec -it python-dev-env bash

# inside container
pip install -r WO-380/requirements.txt
python WO-380/app.py 7.pdf
```

Ports exposed (if needed later): 8000, 5000, 8888.

---

## 📁 Project Structure (selected)

```
WO-380/
├── app.py                 # CLI entrypoint
├── gemini_vision.py       # Gemini Vision integration
├── llm_handler.py         # LLM workflow
├── llm_service.py         # LLM service helpers
├── embedding_service.py   # Embeddings
├── vector_db.py           # ChromaDB integration
├── pdf_to_image.py        # PDF/image utilities
├── prompt.py              # Prompt templates
├── uploads/               # Place PDFs here
├── reports/               # Generated markdown reports
├── chroma_db/             # Vector DB data (gitignored)
├── convertedimages/       # Generated images (gitignored)
├── RESULT/                # Legacy/exported reports (gitignored)
└── requirements.txt
```

> Note: Large/binary/data folders (e.g., `uploads/`, `reports/`, `chroma_db/`, `convertedimages/`, `RESULT/`) are ignored by git via `.gitignore`.

---

## 🐛 Troubleshooting

- **File not found**: Ensure the PDF is inside `WO-380/uploads/` and pass the exact filename.
- **Missing API key**: Create `.env` with `GEMINI_API_KEY` at the repo root.
- **ChromaDB errors**: Delete and re-create `WO-380/chroma_db/` if the index is corrupted.

---

## 🤝 Contributing

1. Create a feature branch
2. Make changes with clear commits
3. Add/update docs where relevant
4. Open a PR

---

Ready to automate your structural design compliance checks? Run `python WO-380/app.py <your-file.pdf>` and get your first report in minutes.