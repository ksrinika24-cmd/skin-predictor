"""
helpers.py

Common helper functions used throughout the Skin Predictor application.
"""

from datetime import datetime
import os


def create_directory(directory_path: str) -> None:
    """
    Create a directory if it does not already exist.

    Args:
        directory_path (str): Path to the directory.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def get_current_timestamp() -> str:
    """
    Returns current timestamp.

    Returns:
        str: Current date and time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_skin_type(skin_type: str) -> str:
    """
    Formats the skin type text.

    Example:
        oily_skin -> Oily Skin
    """
    return skin_type.replace("_", " ").title()


def validate_image_extension(filename: str) -> bool:
    """
    Validate uploaded image extension.

    Supported:
        jpg
        jpeg
        png

    Returns:
        bool
    """
    allowed_extensions = {"jpg", "jpeg", "png"}

    extension = filename.split(".")[-1].lower()

    return extension in allowed_extensions


def confidence_percentage(confidence: float) -> str:
    """
    Convert confidence score to percentage.

    Example:
        0.94 -> 94.00%
    """
    return f"{confidence * 100:.2f}%"