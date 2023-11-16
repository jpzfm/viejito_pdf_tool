import os
import pikepdf

# Function to remove password from pdf
def remove_password(filename, password=None):
    with pikepdf.open(filename, password=password) as pdf:
        pdf.save(filename)

# Function to merge pdfs
def merge_pdfs(input_dir):
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]
    pdf_files.sort()
    output_pdf = pikepdf.Pdf.new()
    for pdf_file in pdf_files:
        pdf = pikepdf.Pdf.open(os.path.join(input_dir, pdf_file))
        output_pdf.pages.extend(pdf.pages)
    output_pdf.save('output.pdf')

# Accepting folder as input
input_dir = '/Users/jose/Desktop/Product Approvals'

# Removing password from password protected pdfs and merging pdfs
for filename in os.listdir(input_dir):
    if filename.endswith('.pdf'):
        filepath = os.path.join(input_dir, filename)
        try:
            remove_password(filepath)
        except:
            pass
merge_pdfs(input_dir)
