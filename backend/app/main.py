# app/main.py

from fastapi import FastAPI

from app.core.database import get_connection



from app.core.db.queries import get_test_users 

app = FastAPI(
    title="DevScope API",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to DevScope API"
    }


@app.get("/health")
def health():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                version = cur.fetchone()[0]

        return {
            "status": "healthy",
            "database": "connected",
            "postgres_version": version,
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e),
        }
@app.get("/users")
def users():

    rows = get_test_users()

    return {
        "users": rows
    }