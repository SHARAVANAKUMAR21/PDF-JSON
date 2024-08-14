import fitz  # PyMuPDF
import os
import base64
import json

def extract_and_encode_images_from_pdf(pdf_path):
    """
    Extracts all images from a PDF file, encodes them in base64, and organizes them hierarchically in a JSON structure.

    Parameters:
    - pdf_path: The path to the PDF file.

    Returns:
    A dictionary with pages as keys and images as values.
    """
    images_data = {}
    doc = fitz.open(pdf_path)
    
    # Extract the directory part of the pdf_path to save images in the same directory
    pdf_directory = os.path.dirname(pdf_path)
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # Load the page
        image_list = page.get_images(full=True)  # Get full info for all images on the page
        
        if image_list:  # Check if there are images on the page
            images_data[page_num] = []  # Initialize the list for this page
            for i, img_info in enumerate(image_list):
                xref = img_info[0]  # xref is the first element in the tuple returned by get_images
                base_image_path = f"image_{page_num}_{i}.png"
                # Construct the full path for the image file correctly
                image_path = os.path.join(pdf_directory, base_image_path)
                
                # Extract the image using its xref and save it directly.
                img_bytes = doc.extract_image(xref=img_info[0])['image']
                
                # Encode the image bytes to base64
                img_base64 = base64.b64encode(img_bytes).decode('utf-8')
                
                # Prepare the image data for JSON
                image_data = {
                    "image_path": image_path,
                    "image_base64": img_base64
                }
                
                images_data[page_num].append(image_data)
    
    # Convert the dictionary to a hierarchical structure
    hierarchical_data = {f"Page {k+1}": v for k, v in images_data.items()}
    
    return hierarchical_data

# Example usage
pdf_path = r'C:\Users\shara\OneDrive\Desktop\ansrsource\Biology2e-WEB_Excerpt.pdf'
images_data = extract_and_encode_images_from_pdf(pdf_path)

# Convert the hierarchical data to JSON and save it to a file
with open('extracted_images_hierarchical.json', 'w') as json_file:
    json.dump(images_data, json_file, indent=4)

print("Images extracted, encoded, and saved in a hierarchical JSON format.")
