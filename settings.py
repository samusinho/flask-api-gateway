import os
from dotenv import load_dotenv

load_dotenv()

URL = os.environ.get("URL")
PORT = int(os.environ.get("PORT"))
