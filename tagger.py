import onnxruntime as ort
import numpy as np
from PIL import Image
import pandas as pd

MODEL_PATH = "models/model.onnx"
TAGS_PATH = "models/selected_tags.csv"

session = ort.InferenceSession(MODEL_PATH)

tags_df = pd.read_csv(TAGS_PATH)

tag_names = tags_df["name"].tolist()


def preprocess(image):

    image = image.resize((448, 448))
    image = np.array(image).astype(np.float32)

    image = image[:, :, ::-1]
    image = image / 255.0

    image = np.expand_dims(image, axis=0)

    return image


def generate_tags(image_path, threshold=0.35):

    image = Image.open(image_path).convert("RGB")

    image = preprocess(image)

    input_name = session.get_inputs()[0].name

    preds = session.run(None, {input_name: image})[0][0]

    result = []

    for i, p in enumerate(preds):

        if p > threshold:
            result.append(tag_names[i])

    return result
