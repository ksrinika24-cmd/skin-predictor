"""
Unit tests for preprocess.py
"""

import numpy as np
from utils.preprocess import preprocess_image


def test_preprocess_shape():
    """Verify image preprocessing output."""

    image = np.zeros((500, 500, 3), dtype=np.uint8)

    processed = preprocess_image(image)

    assert processed.shape == (1, 224, 224, 3)