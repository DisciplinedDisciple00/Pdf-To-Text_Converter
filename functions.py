from pypdf import PdfReader
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes
import pytesseract as pyts


#Finding length of doc for slider limit
def len_finder(file):
    reader = PdfReader(file)
    file_pages = reader.pages

    max_pages = len(file_pages)
    return max_pages


#OCR Extraction
def ocr_extraction(image):
    page_img_text = pyts.image_to_string(image)
    cleaned_page_image_text = page_img_text.split("\n\n")
    return cleaned_page_image_text


#Main text extraction
def converter(file, targets):
    reader = PdfReader(file)
    file_pages = reader.pages

    file_bytes = file.getvalue()
    image_pages = convert_from_bytes(file_bytes)

    cleaned_pages_text = []

    start = targets[0]
    end = targets[1]

    #Text Pre-processing
    for i in range(start-1, end):
        page_text = file_pages[i].extract_text()

        page_image = image_pages[i]

        if page_text is None or page_text == "":
            img_text = ocr_extraction(page_image)
            cleaned_pages_text.append(img_text)
        else:
            cleaned_page_text = page_text.split("\n\n")
            cleaned_pages_text.append(cleaned_page_text)

    return cleaned_pages_text