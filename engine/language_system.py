import json
import os

class LanguageSystem:
    def __init__(self, language):
        self.language = language
        self.translations = self.load_language_file()

    def load_language_file(self):
        path = f"data/{self.language}.json"
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def get(self, key):
        return self.translations.get(key, key)