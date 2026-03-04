import json
import os

SAVE_FILE = "language_save.json"

def save_language(language):
    with open(SAVE_FILE, "w") as f:
        json.dump({"language": language}, f)

def load_language():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            return data.get("language", "en")
    return "en"