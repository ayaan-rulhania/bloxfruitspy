# player/levels.py

class LevelManager:
    """Handles XP, character leveling, and attribute allocation."""
    def __init__(self, player):
        self.player = player
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.xp_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp = 0
        self.xp_to_next_level *= 1.5
        print(f"Leveled up! Player is now level {self.level}")