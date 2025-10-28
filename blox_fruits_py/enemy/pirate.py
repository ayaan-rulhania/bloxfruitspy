# enemy/pirate.py
from .base_enemy import BaseEnemy
from ..settings import *
class Pirate(BaseEnemy):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, health=50, speed=ENEMY_SPEED * 0.8)
        self.image.fill(BLUE) # Blue tint for Pirate