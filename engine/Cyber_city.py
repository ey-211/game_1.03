import json
import os

class SaveSystem:
    def __init__(self):
        self.save_file = "data/savegame.json"
        self.settings_file = "data/settings.json"
    
    def save_game(self, score, health, language, music_volume):
        data = {
            "score": score,
            "health": health,
            "Language": language,
            "music_volume": music_volume
        }
        with open(self.save_file, "w") as f:
             json.dump(data, f, indent=4)
        print("spiel gespeichert!")
    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, "r") as f:
                  return json.load(f)
        return{"language": "de", "music_volume": 50}
