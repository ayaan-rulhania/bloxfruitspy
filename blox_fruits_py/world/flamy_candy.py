# world/flamy_candy.py
import pygame as pg

class FlamyCandy:
    """A specific map/location in the game."""
    def __init__(self, game):
        self.game = game
        self.name = "Flamy Candy Land"

    def draw_map(self, surface):
        surface.fill((255, 160, 128)) # Peachy/Orange color