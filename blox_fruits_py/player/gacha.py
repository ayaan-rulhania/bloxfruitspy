# player/gacha.py
import random

class Gacha:
    """Handles random fruit/item drawing mechanics."""
    def __init__(self, game):
        self.game = game
        self.fruit_pool = ["Kizami", "Flame", "Ice", "Default"]

    def pull(self):
        # Placeholder cost of 50 money
        if self.game.player.money >= 50:
            self.game.player.money -= 50
            fruit = random.choice(self.fruit_pool)
            print(f"You pulled a: {fruit}!")
            return fruit
        else:
            print("Not enough money for a pull!")
            return None