"""
Unit tests for predictor.py
"""

import numpy as np
from unittest.mock import patch
from utils.predictor import predict_skin


@patch("utils.predictor.session")
def test_predict_skin(mock_session):
    """Test skin prediction."""

    mock_session.get_inputs.return_value = [type("", (), {"name": "input"})()]
    mock_session.run.return_value = [
        np.array([[0.05, 0.10, 0.75, 0.05, 0.05]])
    ]

    image = np.zeros((224, 224, 3), dtype=np.uint8)

    skin_type, confidence = predict_skin(image)

    assert skin_type == "Oily"
    assert confidence > 0