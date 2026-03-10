import os
import torch
import clip
import faiss
import pickle
from PIL import Image
import numpy as np

device = "cuda" if torch.cuda.is_available() else "cpu"

model, preprocess = clip.load("ViT-B/32", device=device)

DATASET_DIR = "dataset"
EMBEDDING_DIR = "embeddings"


def build_index():

    image_paths = []
    features = []

    os.makedirs(EMBEDDING_DIR, exist_ok=True)

    for file in os.listdir(DATASET_DIR):

        if file.lower().endswith(("png", "jpg", "jpeg")):

            path = os.path.join(DATASET_DIR, file)

            image = preprocess(Image.open(path)).unsqueeze(0).to(device)

            with torch.no_grad():
                feature = model.encode_image(image)

            feature = feature.cpu().numpy()

            features.append(feature[0])
            image_paths.append(file)

    if len(features) == 0:
        print("dataset is empty")
        return

    features = np.array(features).astype("float32")

    index = faiss.IndexFlatL2(features.shape[1])
    index.add(features)

    faiss.write_index(index, f"{EMBEDDING_DIR}/index.faiss")

    with open(f"{EMBEDDING_DIR}/meta.pkl", "wb") as f:
        pickle.dump(image_paths, f)

    print("Index created:", len(image_paths))


def search_similar(image_path, top_k=5):

    index = faiss.read_index("embeddings/index.faiss")

    with open("embeddings/meta.pkl", "rb") as f:
        image_paths = pickle.load(f)

    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)

    with torch.no_grad():
        feature = model.encode_image(image)

    feature = feature.cpu().numpy().astype("float32")

    D, I = index.search(feature, top_k)

    results = []

    for i in I[0]:
        results.append(image_paths[i])

    return results
