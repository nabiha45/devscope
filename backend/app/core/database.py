# app/core/database.py

import psycopg

from app.core.config import settings


def get_connection():
    """
    Create and return a PostgreSQL connection.
    """

    return psycopg.connect(
        settings.DATABASE_URL,
        autocommit=True,
    )