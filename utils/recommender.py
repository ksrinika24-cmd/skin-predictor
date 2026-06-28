"""
recommender.py

Recommendation Engine
"""

import pandas as pd


DATASET = "data/recommendations.csv"


recommendations = pd.read_csv(DATASET)


def recommend(skin_type):

    result = recommendations[
        recommendations["SkinType"] == skin_type
    ]

    return result.to_dict(orient="records")