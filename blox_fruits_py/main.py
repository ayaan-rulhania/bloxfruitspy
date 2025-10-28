# main.py
import pygame as pg
from .pirate_game_loop import Game

def main():
    """Main entry point of the game."""
    g = Game()

    while g.running:
        g.new()

    pg.quit()

if __name__ == '__main__':
    main()