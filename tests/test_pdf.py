"""
Unit tests for pdf_report.py
"""

import os

from utils.pdf_report import generate_report


def test_pdf_generation():

    filename = "reports/test_report.pdf"

    os.makedirs("reports", exist_ok=True)

    generate_report(
        filename,
        "Oily",
        0.96
    )

    assert os.path.exists(filename)