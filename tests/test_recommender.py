"""
Unit tests for recommender.py
"""

from utils.recommender import recommend


def test_recommend_returns_list():
    """Recommendation engine returns list."""

    result = recommend("Oily")

    assert isinstance(result, list)