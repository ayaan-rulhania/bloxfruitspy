# player/shop.py

class Shop:
    """Manages buying and selling items, fruits, and upgrades."""
    def __init__(self, game):
        self.game = game
        self.inventory = {}

    def open_shop(self):
        print("Shop opened: Welcome! (UI to be implemented)")