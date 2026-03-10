from fastapi import FastAPI, UploadFile, File
import shutil
import os

from indexer import build_index, search_similar
from tagger import generate_tags

app = FastAPI()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.on_event("startup")
def startup():

    print("Building dataset index...")
    build_index()


@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    tags = generate_tags(file_path)

    similar = search_similar(file_path)

    return {
        "tags": tags,
        "similar_images": similar
    }
