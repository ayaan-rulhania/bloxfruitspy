# world/re_glacier.py
import pygame as pg

class ReGlacier:
    """A specific map/location in the game."""
    def __init__(self, game):
        self.game = game
        self.name = "Re-Glacier"

    def draw_map(self, surface):
        surface.fill((200, 200, 255)) # Light blue/ice color