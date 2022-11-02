import os
from dotenv import load_dotenv

load_dotenv()

URL = os.environ.get("URL")
PORT = int(os.environ.get("PORT"))
VOTES_URL = os.environ.get("VOTES_URL")
SECURITY_URL = os.environ.get("SECURITY_URL")
