import time
from engine.attack_system import AttackSystem
from engine.save_system import SaveSystem

class GameEngine:
    def __init__(self):
        self.score = 0
        self.health = 100
        self.attack_system = AttackSystem()
        self.save_system = SaveSystem()
        self.language = "de"
        self.music_volume = 50    # kommt noch

        def load_settings(self):
            settings = self.save_system.load_settings()
            self.language = settings.get("language", "de")
            self.music_volume = settings.get("music_volume", 50)

        def run(self):
            print(f"Sprache: {self.lanuage}, Musiklautstärke: {self.music_volume}")
            print("Spiel startet...\n")

            for minute in range(1, 6): 
                print(f"---Minute {minute} ---")
                attacks = self.attack_system.generate_attacks(minute)
                for attack in attacks:
                    print(f"[ALERT] {attack}")
                self.score += len(attacks) * 10
                print(f"Score: {self.score}, health: {self.health}\n")
                time.sleep(1)  

            print("Simulation beendet!")
            self.save_system.save_game(self.score, self.health, self.language, self.music_volume)