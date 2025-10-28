# player/player.py
import pygame as pg
from ..settings import *
from ..utils import load_image

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 2
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.image = load_image('placeholder.png')
        self.image = pg.transform.scale(self.image, (48, 48))
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        self.rect.topleft = (x, y)
        self.health = PLAYER_HEALTH
        self.money = STARTING_MONEY

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED

        # Diagonal movement compensation
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.707
            self.vy *= 0.707

    def update(self):
        self.get_keys()

        # Apply movement
        self.x += self.vx
        self.y += self.vy

        # Simple boundary check
        self.x = max(0, min(self.x, SCREEN_WIDTH - self.rect.width))
        self.y = max(0, min(self.y, SCREEN_HEIGHT - self.rect.height))

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)