import time
import engine.language_system
from engine.attack_system import AttackSystem
import engine.save_system


class GameEngine:

    def __init__(self):
        self.score = 0
        self.health = 100
        self.attack_system = AttackSystem()
        self.save_system = engine.save_system.SaveSystem()

        # Settings laden
        settings = self.save_system.load_settings()
        self.language = settings.get("language", "de")
        self.music_volume = settings.get("music_volume", 50)
        self.language_system = engine.language_system.LanguageSystem(self.language)
       
    def run(self):

        print(self.language_system.get("welcome"))
        print(self.language_system.get("simulation_start"))
        print()

        for minute in range(1, 6):

            print(f"{self.language_system.get('minute')} {minute}")

            attacks = self.attack_system.generate_attacks(minute)

            for attack in attacks:
                print(f"[ALERT] {attack}")

            self.score += len(attacks) * 10

            print(f"{self.language_system.get('score')}: {self.score}")
            print()

            time.sleep(1)

        print(self.language_system.get("simulation_end"))

        self.save_system.save_game(
            self.score,
            self.health,
            self.language,
            self.music_volume
        )