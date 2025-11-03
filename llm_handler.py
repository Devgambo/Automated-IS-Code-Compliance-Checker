import os
import base64
import io
from openai import OpenAI
from dotenv import load_dotenv
import fitz  # PyMuPDF
from PIL import Image

# Load environment variables from .env file
load_dotenv()

def pdf_to_images(pdf_path):
    """Converts each page of a PDF into a list of PIL Image objects."""
    images = []
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            # Higher DPI for better quality
            pix = page.get_pixmap(dpi=200)
            img_data = pix.tobytes("png")
            image = Image.open(io.BytesIO(img_data))
            images.append(image)
        doc.close()
    except Exception as e:
        print(f"Error processing PDF file: {e}")
        raise
    return images

def pil_to_base64(image):
    """Converts a PIL Image to a base64 encoded string."""
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def analyze_rcc_drawing(pdf_path, prompt_text):
    """
    Analyzes an RCC drawing PDF using the OpenRouter API.

    Args:
        pdf_path (str): The path to the PDF file.
        prompt_text (str): The text prompt to guide the analysis.

    Returns:
        str: The generated text response from the model.
    """
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in .env file.")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    try:
        print(f"Converting PDF '{pdf_path}' to images...")
        images = pdf_to_images(pdf_path)
        print(f"Successfully converted {len(images)} pages to images.")

        base64_images = [pil_to_base64(img) for img in images]

        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt_text},
                ] + [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{img}"
                        }
                    } for img in base64_images
                ]
            }
        ]

        print("Sending request to OpenRouter...")
        response = client.chat.completions.create(
            model="google/gemini-2.5-flash-preview-09-2025",
            messages=messages,
            max_tokens=12000, # Set a higher limit for detailed reports
        )
        print("Received response from OpenRouter.")
        
        return response.choices[0].message.content

    except Exception as e:
        print(f"An error occurred during the analysis: {e}")
        return f"Error: Could not analyze the PDF. {e}"