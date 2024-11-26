import fitz  # PyMuPDF
from PIL import Image
import pytesseract


with fitz.open("Attention Is All You Need.pdf") as doc:
    for page in doc:
        print(page.get_text())

# text = pytesseract.image_to_string(Image.open("scanned_sample.pdf"))
# print(text)

#mongodb+srv://omrisa:wC2QLi8rK62NTcvW@cluster0.x31xf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0