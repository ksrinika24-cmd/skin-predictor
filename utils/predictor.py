"""
predictor.py

Skin type prediction.
"""

import numpy as np

from utils.model_loader import load_model
from utils.preprocess import preprocess_image


LABELS = [
    "Dry",
    "Normal",
    "Oily",
    "Combination",
    "Sensitive",
]


session = load_model()


def predict_skin(image):

    processed = preprocess_image(image)

    input_name = session.get_inputs()[0].name

    output = session.run(
        None,
        {input_name: processed}
    )[0]

    prediction = np.argmax(output)

    confidence = float(np.max(output))

    return LABELS[prediction], confidence