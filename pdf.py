import fitz  # PyMuPDF
import base64
import json
import os
from pydantic import BaseModel

class PageData(BaseModel):
    text_blocks: list[str]
    images: list[dict[str, str]]
    tables: list[list[list[str]]]  # Simplified representation of tables

class DocumentData(BaseModel):
    pages: dict[int, PageData]


def extract_tables_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    tables_data = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        table_data = []

        # Analyze the layout to identify potential tables
        for block in page.get_text("dict")["blocks"]:
            if block["type"] == 0:  # Assuming block type 0 represents text
                continue

            # Placeholder for logic to analyze and group cells
            # This is highly dependent on the specific layout and structure of your PDFs
            # You'll need to implement the logic to analyze bboxes and group cells accordingly

        tables_data.append(table_data)

    return tables_data


def extract_text_and_images_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    document_data = DocumentData(pages={})

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text_blocks = []
        images = []
        tables = []

        # Extract text
        for block in page.get_text("dict")["blocks"]:
            if block["type"] == 0:  # Block type 0 indicates text
                lines = [" ".join(line["spans"][0]["text"]) for line in block["lines"]]
                text_blocks.extend(lines)

        # Extract images
        for img in page.get_images(full=True):
            xref = img[0]
            base_image_path = f"image_{xref}.png"
            img_bytes = doc.extract_image(xref=xref)["image"]

            # Encode the image bytes to base64
            img_base64 = base64.b64encode(img_bytes).decode('utf-8')

            images.append({"image_path": base_image_path, "image_base64": img_base64})

        # Extract tables (simplified example)
        # This is a placeholder for table extraction logic
        # You'll need to implement a more sophisticated approach based on your PDFs
        tables.append([])  # Placeholder for table data

        document_data.pages[page_num] = PageData(text_blocks=text_blocks, images=images, tables=[tables])

    return document_data

def save_to_json(data, file_name):
    data_dict = data.dict()
    with open(file_name, 'w') as json_file:
        json.dump(data_dict, json_file, indent=4)

# Example usage
pdf_path = r"C:\Users\shara\OneDrive\Desktop\ansrsource\Biology2e-WEB_Excerpt.pdf"
data = extract_text_and_images_from_pdf(pdf_path)
save_to_json(data, "output.json")

print("Text, images, and tables extracted and saved in a hierarchical JSON format.")
