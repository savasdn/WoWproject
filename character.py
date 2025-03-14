from random import randrange

class Character:

    def __init__(self, name, attack_speed = 2, delay = 0):
        self.name = name
        self.health = 100
        self.attack_speed = attack_speed
        self.delay = delay

    def attack(self):
        self.delay = 5 - self.attack_speed
        return randrange(3,11)

    def is_dead(self):
        return self.health <= 0

    def end_round(self):
        self.health += 1 if self.health+1 <= 100 else 0
        self.delay -= 1

    def print(self):
        print(f"{self.name} -- H: {self.health} ATCK_SPEED: {self.attack_speed} D: {self.delay}")

p1 = Character("Kuoga")
p1.attack()
p1.end_round()
p1.print()
