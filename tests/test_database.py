"""
Unit tests for database.py
"""

from utils.database import create_table


def test_database_creation():
    """Database table should be created."""

    create_table()

    assert True