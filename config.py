import os
from dotenv import load_dotenv

load_dotenv()

DOMAIN = os.getenv("HOST_URL")
DATABASE = os.getenv("DATABASE")
SECRET_KEY = os.getenv("SECRET_KEY")