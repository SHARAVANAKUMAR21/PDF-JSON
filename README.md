# PDF to JSON Converter

This Python application reads a PDF file, extracts structured data from it, and converts this data into a JSON format using Pydantic models for data validation and serialization.

## Description

The PDF to JSON Converter streamlines the process of extracting data from PDF files and converting it into a structured JSON format. The tool handles various types of data within a PDF, including tables, text blocks, and images. Using `pdfplumber` for PDF manipulation and `pydantic` for data validation and serialization, the application ensures that the extracted data is accurate and well-structured.

## Features

- **PDF Reading:** Reads PDF files using `pdfplumber`.
- **Data Extraction:** Extracts tables, text blocks, and images from PDFs.
- **Data Validation and Serialization:** Validates and serializes the extracted data into JSON format using Pydantic models.
- **Output:** Generates a JSON file containing the structured data extracted from the PDF.

## Approach

1. **PDF Reading:**
   - Utilizes `pdfplumber` to open and read the PDF file, handling exceptions appropriately.

2. **Data Extraction:**
   - **Title:** Extracts from the first line of text on the first page.
   - **Text Blocks:** Converts text into `TextBlock` objects.
   - **Tables:** Converts extracted tables into `Table` objects.
   - **Images:** Extracts images as `ImageBlock` objects (implementation in progress).

3. **Data Validation and Serialization:**
   - Uses Pydantic models (`PDFData`, `Table`, `TextBlock`, `ImageBlock`) for validating and serializing data to JSON.

4. **Execution:**
   - The `main` function handles reading the PDF, extracting data, and serializing it to JSON.

## Requirements

- `Python` 3.7+ (3.12.4 recommended)
- `pdfplumber` library
- `pydantic` library
- `streamlit` library (for running the Streamlit app)

## Setup

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/SHARAVANAKUMAR21/PDF_to_JSON.git
cd PDF_to_JSON
```
### Step 2: Install Dependencies

Create a virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```
### Step 4: Upload a PDF File

1. Open your web browser and navigate to the local URL provided by Streamlit.
2. Click on the file uploader widget to upload a PDF file.
3. Once the PDF is uploaded, the application will process the file and generate a JSON file containing the extracted data.
4. You will be able to download the JSON file directly from the Streamlit interface.


### Step 3: Run the Application

To start the Streamlit app, use the following command:

```bash
streamlit run pdf3.py
```

## Contact

For any questions or feedback, please reach out to:

- **Name:** Saravanan Kumar B
- **Email:** saravana.kb21@outlook.com
