# utils.py
import pygame as pg
import os
import sys
from .settings import WHITE, RED

def load_image(filename):
    """Loads an image from the assets folder."""
    # The path should be relative to the main game directory
    assets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets')
    path = os.path.join(assets_dir, filename)

    # Try to load the image
    if not os.path.exists(path):
        # Fallback: Create a simple placeholder image
        print(f"Warning: Image file not found: {path}. Using placeholder.")
        temp_surface = pg.Surface((32, 32)).convert_alpha()
        temp_surface.fill(RED)
        pg.draw.rect(temp_surface, WHITE, temp_surface.get_rect(), 1)
        return temp_surface

    try:
        image = pg.image.load(path).convert_alpha()
        return image
    except pg.error as e:
        print(f"Error loading image {path}: {e}")
        sys.exit()