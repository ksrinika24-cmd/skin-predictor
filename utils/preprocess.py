"""
preprocess.py

Image preprocessing for Skin Predictor.
"""

import cv2
import numpy as np


IMAGE_SIZE = (224, 224)


def preprocess_image(image):
    """
    Preprocess image before prediction.

    Steps:
        Resize
        RGB Conversion
        Normalize
        Expand Dimensions
    """

    image = cv2.resize(image, IMAGE_SIZE)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = image.astype(np.float32)

    image = image / 255.0

    image = np.expand_dims(image, axis=0)

    return image