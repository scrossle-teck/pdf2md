
from PyPDF2 import PdfReader

def greet(name: str = "Template") -> str:
    return f"Hello, {name}!"

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts all text from a PDF file using PyPDF2.
    """
    reader = PdfReader(pdf_path)
    text = []
    for page in reader.pages:
        text.append(page.extract_text() or "")
    return "\n".join(text)



def main() -> None:
    message = greet()
    print(message)


if __name__ == "__main__":
    main()
