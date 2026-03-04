import random

class AttackSystem:
    def __init__(self):
        self.attack_types = [
            "Port Scan erkannt",
            "brute force angriff",
            "malware traffic",
            "phishing E-mail"
        ]
    def generate_attacks(self, minute):
        count = random.randint(1, minute + 1)
        return random.choices(self.attack_types, k=count)