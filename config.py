import os
from dotenv import load_dotenv

load_dotenv()

DOMAIN: str = os.getenv("HOST_URL") # type: ignore
DATABASE: str = os.getenv("DATABASE") # type: ignore
SECRET_KEY: str = os.getenv("SECRET_KEY") # type: ignore
MAX_INPUT_LENGTH: int = 4000