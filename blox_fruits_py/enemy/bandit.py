# enemy/bandit.py
from .base_enemy import BaseEnemy # Use '.' for local imports within the 'enemy' folder
# FIX: Use '..' for relative import to the parent directory for settings
from ..settings import *
class Bandit(BaseEnemy):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, health=30, speed=ENEMY_SPEED * 1.2)
        self.image.fill(YELLOW) # Yellow tint for Bandit