from app.core.database import get_connection


def get_test_users():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, name, age
                FROM test_users
                ORDER BY id;
            """)

            rows = cur.fetchall()

    return rows