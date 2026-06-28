"""
pdf_report.py

Generate PDF report.
"""

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


def generate_report(filename, skin_type, confidence):

    document = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("<b>Skin Predictor Report</b>", styles["Title"]))

    elements.append(Paragraph(f"Skin Type: {skin_type}", styles["BodyText"]))

    elements.append(Paragraph(f"Confidence: {confidence:.2f}", styles["BodyText"]))

    document.build(elements)