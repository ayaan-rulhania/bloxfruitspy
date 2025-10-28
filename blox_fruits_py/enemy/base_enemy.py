# enemy/base_enemy.py
import pygame as pg
from ..settings import ENEMY_SPEED
from ..utils import load_image

class BaseEnemy(pg.sprite.Sprite):
    def __init__(self, game, x, y, health=20, speed=ENEMY_SPEED, image_file='placeholder.png'):
        self._layer = 1
        self.groups = game.all_sprites, game.enemies
        pg.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.image = load_image(image_file)
        self.image = pg.transform.scale(self.image, (32, 32))
        self.image.fill((255, 0, 0, 150)) # Red tint for enemies (with transparency)
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        self.rect.topleft = (x, y)
        self.health = health
        self.speed = speed

    def follow_player(self):
        """Simple AI to move toward the player."""
        dx = self.game.player.x - self.x
        dy = self.game.player.y - self.y

        distance = (dx**2 + dy**2)**0.5

        if distance > 1:
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed
            self.rect.x = int(self.x)
            self.rect.y = int(self.y)

    def update(self):
        self.follow_player()
        if self.health <= 0:
            self.kill()