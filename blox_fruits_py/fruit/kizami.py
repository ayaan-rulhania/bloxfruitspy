# fruit/kizami.py
from .base_fruit import BaseFruit

class Kizami(BaseFruit):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, name="Kizami Fruit", power_level=5)
        self.image.fill((255, 100, 0)) # Orange tint

    def use_power(self, player):
        """Gives the player a temporary speed boost."""
        # You'd need to add logic to player.py to handle the boost, but for now:
        print(f"Player used {self.name} and gained a speed boost!")