"""
database.py

SQLite database for prediction history.
"""

import sqlite3


DATABASE = "data/users.db"


def create_connection():

    return sqlite3.connect(DATABASE)


def create_table():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skin_type TEXT,
            confidence REAL,
            created_at TEXT
        )
    """)

    conn.commit()

    conn.close()


def save_prediction(
    skin_type,
    confidence,
    created_at
):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO history(
            skin_type,
            confidence,
            created_at
        )
        VALUES (?, ?, ?)
    """, (skin_type, confidence, created_at))

    conn.commit()

    conn.close()