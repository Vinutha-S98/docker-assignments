import os
import pymysql
from fastapi import FastAPI, HTTPException
from datetime import datetime
from pymysql.err import OperationalError

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "visitdb")

app = FastAPI()

def get_db_connection():
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except OperationalError as e:
        raise HTTPException(status_code=500, detail=f"DB connection failed: {str(e)}")

def init_db():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS visits (
                id INT AUTO_INCREMENT PRIMARY KEY,
                visit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    conn.commit()
    conn.close()

@app.on_event("startup")
async def startup():
    init_db()

@app.get("/")
async def root():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO visits () VALUES ()")
            conn.commit()
            cursor.execute("SELECT COUNT(*) AS total FROM visits")
            total = cursor.fetchone()["total"]

            cursor.execute("""
                SELECT DATE(visit_time) as date, COUNT(*) as count 
                FROM visits 
                GROUP BY DATE(visit_time)
                ORDER BY DATE(visit_time)
            """)
            breakdown = cursor.fetchall()
        conn.close()
        return {
            "total_visits": total,
            "breakdown": {entry["date"].isoformat(): entry["count"] for entry in breakdown}
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
