import random

class AttackSystem:
    def __init__(self):
        self.attack_types = [
            "Port Scan",
            "Brute Force Login",
            "Malware Traffic",
            "Phishing Email"
        ]

    def generate_attacks(self, minute):
        count = random.randint(minute, minute + 2)

        attacks = []
        for _ in range(count):
            attack = random.choice(self.attack_types)

            ip = f"{random.randint(10,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
            port = random.choice([22, 80, 443, 3389])

            attacks.append({
                "type": attack,
                "ip": ip,
                "port": port
            })

        return attacks