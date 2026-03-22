import time
import engine.attack_system
import engine.save_system

class Colors:
    RED = '\033[91m'
    RESET = '\033[0m'


class GameEngine:

    correct_actions = {
        "Phishing Email": "3",
        "Brute Force Login": "1",
        "Malware Traffic": "1",
        "Port Scan": "3"
    }

    def __init__(self):
        import engine.language_system
        self.score = 0
        self.health = 100
        self.attack_system = engine.attack_system.AttackSystem()
        self.save_system = engine.save_system.SaveSystem()

        settings = self.save_system.load_settings()
        self.language = settings.get("language", "de")
        self.music_volume = settings.get("music_volume", 50)
        self.language_system = engine.language_system.LanguageSystem(self.language)

    def run(self):
        print("CONNECTING TO SOC SYSTEM...")
        print("ACCESS GRANTED\n")

        for minute in range(1, 6):
            print(f"\nMINUTE {minute}")

            attacks = self.attack_system.generate_attacks(minute)

            for attack in attacks:
             print(f"{Colors.RED}ALERT: {attack['type']} | IP: {attack['ip']} | Port: {attack['port']}{Colors.RESET}")   

            print("\n1 = Block")
            print("2 = Ignore")
            print("3 = Analyse")

            choice = input(">>> ")

            for attack in attacks:
                correct = self.correct_actions.get(attack["type"])

                if choice == correct:
                    print(f"✔ {attack['type']} abgewehrt")
                    self.score += 10
                else:
                    print(f"❌ Fehler bei {attack['type']}")
                    self.health -= 10

            print(f"Health: {self.health}")
            print(f"Score: {self.score}")

            if self.health <= 0:
                print("💀 GAME OVER")
                return

            time.sleep(1)

        print("🎉 YOU WIN")