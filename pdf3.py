import base64
import fitz  # PyMuPDF
from pydantic import BaseModel
import json
import streamlit as st
from io import BytesIO

class ImageData(BaseModel):
    image_path: str
    image_base64: str

class TableData(BaseModel):
    rows: list[list[str]]  # Simplified; actual implementation depends on PDF structure

class PageData(BaseModel):
    text_blocks: list[str]
    images: list[ImageData]
    tables: list[TableData]

class DocumentData(BaseModel):
    pages: dict[int, PageData]

def extract_text_and_images_from_pdf(pdf_data):
    doc = fitz.open(stream=pdf_data, filetype="pdf")
    document_data = DocumentData(pages={})

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text_blocks = []
        images = []
        tables = []  # Placeholder for actual table extraction logic

        # Extract text blocks
        for block in page.get_text("dict")["blocks"]:
            if block["type"] == 0:  # Assuming block type 0 indicates text
                block_text = " ".join([span["text"] for line in block["lines"] for span in line["spans"]])
                text_blocks.append(block_text)

        # Extract images
        for img in page.get_images(full=True):
            xref = img[0]
            img_data = doc.extract_image(xref)
            img_bytes = img_data["image"]
            img_base64 = base64.b64encode(img_bytes).decode('utf-8')
            image_path = f"image_{xref}.png"
            images.append(ImageData(image_path=image_path, image_base64=img_base64))

        # Placeholder for table extraction logic
        # This is a conceptual approach and will need significant customization
        tables.append(TableData(rows=[]))  # Adjusted to match the expected structure

        document_data.pages[page_num] = PageData(text_blocks=text_blocks, images=images, tables=tables)

    return document_data

def main():
    st.title("PDF Text and Image Extraction")

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_file is not None:
        pdf_data = uploaded_file.read()
        data = extract_text_and_images_from_pdf(pdf_data)

        # Convert the extracted data to JSON
        json_data = json.dumps(data.dict(), indent=4)
        
        # Provide an option to download the JSON data at the top
        st.download_button(
            label="Download JSON",
            data=json_data,
            file_name="extracted_data.json",
            mime="application/json",
            help="Click to download the extracted data as JSON"
        )
        
        # Display the JSON data in Streamlit
        st.subheader("Extracted Data")
        st.json(json_data)

if __name__ == "__main__":
    main()
