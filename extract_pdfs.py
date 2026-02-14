import os
import pdfplumber

PDF_DIR = r"C"

all_text = ""

for filename in os.listdir(PDF_DIR):
    if filename.lower().endswith(".pdf"):
        full_path = os.path.join(PDF_DIR, filename)
        print(f"Processing: {full_path}")

        with pdfplumber.open(full_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    all_text += f"\n\n--- FILE: {filename} ---\n\n"
                    all_text += text

output_dir = r"C"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(PDF_DIR):
    if filename.endswith(".pdf"):
        full_path = os.path.join(PDF_DIR, filename)

        text_content = ""
        with pdfplumber.open(full_path) as pdf:
            for page in pdf.pages:
                if page.extract_text():
                    text_content += page.extract_text() + "\n"

        out_file = os.path.join(output_dir, filename.replace(".pdf", ".txt"))
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(text_content)