"""
model_loader.py

Loads ONNX model for offline inference.
"""

import onnxruntime as ort


MODEL_PATH = "models/skin_classifier.onnx"


def load_model():
    """
    Load ONNX model.

    Returns:
        ONNX Runtime session.
    """
    session = ort.InferenceSession(
        MODEL_PATH,
        providers=["CPUExecutionProvider"]
    )

    return session