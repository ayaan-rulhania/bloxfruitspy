# fruit/base_fruit.py
import pygame as pg
from ..utils import load_image # FIX: Use '..' for relative import

class BaseFruit(pg.sprite.Sprite):
    def __init__(self, game, x, y, name="Fruit", power_level=1):
        self._layer = 1
        self.groups = game.all_sprites, game.fruits
        pg.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.name = name
        self.power_level = power_level

        self.image = load_image('placeholder.png')
        self.image = pg.transform.scale(self.image, (24, 24))
        self.image.fill((0, 255, 0, 150)) # Green tint for all fruits

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def use_power(self, player):
        """Abstract method for the fruit's special ability."""
        print(f"{self.name} power used! This should be overridden.")

    def update(self):
        pass