import os
from dotenv import load_dotenv

load_dotenv()
api_status = os.getenv("API_KEY")

if api_status :
    print(True)
    print("API key configured")
else:
    print(False)
    print("API key missing")

