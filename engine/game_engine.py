import time
import engine.language_system
from .attack_system import AttackSystem
import engine.save_system

class Colors:
    RED = "\033[31m"
    GREEN = "\033[32m"
    CYAN = "\033[36m"
    RESET = "\033[0m"


class GameEngine:

    def __init__(self):
        self.score = 0
        self.health = 100
        self.attack_system = AttackSystem()
        self.save_system = engine.save_system.SaveSystem()

        
        settings = self.save_system.load_settings()
        self.language = settings.get("language", "de")
        self.music_volume = settings.get("music_volume", 50)
        self.language_system = engine.language_system.LanguageSystem(self.language)
        
    def run(self):
        print(self.language_system.get("welcome"))

        correct_actions = {
            "phishing E-mail": "3",
            "brute force angriff": "1",
            "malware traffic": "1",
            "Port Scan erkannt": "3"
        }

        for minute in range(1, 6):
            print(f"{self.language_system.get('minute')} {minute}")

            attacks = self.attack_system.generate_attacks(minute)

            for attack in attacks:
                print(f"[ALERT] {attack}")

            print()
            print("Was willst du tun?")
            print("1 = Blocken")
            print("2 = Ignorieren")
            print("3 = Analysieren")

            choice = input("Deine Entscheidung: ")

            for attack in attacks:
                correct = correct_actions.get(attack)

                if choice == correct:
                    print(f"Richtig reagiert auf {attack} ✅")
                    self.score += 10
                else:
                    print(f"Falsche Reaktion auf {attack} ❌")
                    self.health -= 10

            print(f"Health: {self.health}")
            print(f"{self.language_system.get('score')}: {self.score}")
            print(f"Score: {self.score}")
            print()

            if self.health <= 0:
                print("GAME OVER 💀")
                break

            time.sleep(1)