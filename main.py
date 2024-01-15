import os
import fitz  # PyMuPDF

def merge_pdfs(input_folder, output_folder, output_filename, title, author):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of PDF files in the input folder
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

    if not pdf_files:
        print("No PDF files found in the input folder.")
        return

    # Create a PdfWriter object to hold the merged PDF
    pdf_writer = fitz.open()

    # Iterate through each PDF file and append its pages to the PdfWriter
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        pdf_document = fitz.open(pdf_path)
        pdf_writer.insert_pdf(pdf_document)

    # Set the title and author properties
    pdf_writer.setMetadata({
        'title': title,
        'author': author
    })

    # Create the output PDF file
    output_path = os.path.join(output_folder, f'{output_filename}.pdf')
    pdf_writer.save(output_path)
    pdf_writer.close()

    print(f'Merged PDF saved to: {output_path}')

if __name__ == "__main__":
    # Provide input folder, output folder, output filename, title, and author
    input_folder = input("Enter the input folder path: ")
    output_folder = input("Enter the output folder path: ")
    output_filename = input("Enter the desired name for the merged PDF file: ")
    title = input("Enter the title for the PDF: ")
    author = input("Enter the author's name for the PDF: ")

    merge_pdfs(input_folder, output_folder, output_filename, title, author)
