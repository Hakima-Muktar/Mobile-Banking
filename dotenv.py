from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()

DB_HOST = os.getenv("localhost")
DB_PORT = os.getenv("5432")
DB_NAME = os.getenv("bank_reviews")
DB_USER = os.getenv("postgres")
DB_PASSWORD = os.getenv("8075")

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print("✔ Connected to PostgreSQL")
