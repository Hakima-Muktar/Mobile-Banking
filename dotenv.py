from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()

host = os.getenv("localhost")
port = os.getenv("5432")
db = os.getenv("mobilebank")
user = os.getenv("hakima")
password = os.getenv("123")

engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
