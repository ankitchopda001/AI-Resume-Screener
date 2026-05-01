import PyPDF2
import docx

def parse_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def parse_docx(file):
    doc = docx.Document(file)
    return " ".join([p.text for p in doc.paragraphs])

# Converts resume → text