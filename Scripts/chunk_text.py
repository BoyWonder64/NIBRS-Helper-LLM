import os
from pathlib import Path

INPUT_DIR = "text_folder"
OUTPUT_DIR = "/chunk_folder"

os.makedirs(OUTPUT_DIR, exist_ok=True)

CHUNK_SIZE = 1000   # characters (starter, not tokens yet)
OVERLAP = 200

def chunk_text(text):
    chunks = []
    start = 0
    while start < len(text):
        end = start + CHUNK_SIZE
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - OVERLAP
    return chunks

for file in os.listdir(INPUT_DIR):
    if file.endswith(".txt"):
        with open(os.path.join(INPUT_DIR, file), "r", encoding="utf-8") as f:
            text = f.read()

        chunks = chunk_text(text)

        base = Path(file).stem
        for i, chunk in enumerate(chunks):
            out_file = f"{base}_chunk_{i}.txt"
            with open(os.path.join(OUTPUT_DIR, out_file), "w", encoding="utf-8") as f:
                f.write(chunk)

        print(f"Chunked {file} into {len(chunks)} parts")
