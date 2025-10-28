# world/pirate_village.py
import pygame as pg

class PirateVillage:
    """The starting map/location in the game."""
    def __init__(self, game):
        self.game = game
        self.name = "Pirate Village"

    def draw_map(self, surface):
        # Draw a simple green background for the village
        surface.fill((34, 139, 34))
        # Draw a patch of water
        pg.draw.rect(surface, (0, 100, 200), (0, 0, 200, 768))