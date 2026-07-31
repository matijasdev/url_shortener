import os
from dotenv import load_dotenv

load_dotenv()

DOMAIN = os.getenv("HOST_URL")
DATABASE = os.getenv("DATABASE")