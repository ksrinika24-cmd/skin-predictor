from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image


def preprocess_image(image: Image.Image) -> np.ndarray:
    rgb = image.convert("RGB").resize((224, 224))
    arr = np.asarray(rgb).astype("float32") / 255.0
    return np.transpose(arr, (2, 0, 1))[None, ...]


def detect_face_status(image: Image.Image) -> str:
    try:
        import cv2
        gray = cv2.cvtColor(np.asarray(image.convert("RGB")), cv2.COLOR_RGB2GRAY)
        cascade_path = Path(cv2.__file__).parent / "data" / "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(str(cascade_path))
        faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
        if len(faces) == 0:
            return "No face detected"
        if len(faces) > 1:
            return "Multiple faces detected"
        return "Single face detected"
    except Exception:
        return "Face detection unavailable"
