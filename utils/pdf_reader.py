"""
PDF Reader Utility
Extracts text from uploaded PDF resume files.
"""

import io
import re


def extract_text_from_pdf(uploaded_file) -> str:
    """
    Extract text content from a PDF file.
    
    Args:
        uploaded_file: Streamlit UploadedFile object
        
    Returns:
        str: Extracted text from the PDF
    """
    text = ""
    
    try:
        import PyPDF2
        
        # Read the uploaded file bytes
        file_bytes = uploaded_file.read()
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        
        # Extract text from all pages
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        
        # Reset file pointer for potential re-use
        uploaded_file.seek(0)
        
    except ImportError:
        try:
            import pdfplumber
            file_bytes = uploaded_file.read()
            with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            uploaded_file.seek(0)
        except ImportError:
            text = "PDF library not available. Please install PyPDF2: pip install PyPDF2"
    
    except Exception as e:
        text = f"Error extracting PDF text: {str(e)}"
    
    return clean_text(text)


def clean_text(text: str) -> str:
    """
    Clean and normalize extracted text.
    
    Args:
        text: Raw extracted text
        
    Returns:
        str: Cleaned text
    """
    if not text:
        return ""
    
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove special characters but keep alphanumeric, spaces, and common punctuation
    text = re.sub(r'[^\w\s\.,\-\+\#\/\@\(\)]', ' ', text)
    
    # Remove excessive spaces again after character removal
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()
