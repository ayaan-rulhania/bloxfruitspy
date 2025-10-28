# player/money.py

class MoneyManager:
    """Simple class to handle all money transactions."""
    def __init__(self, player):
        self.player = player

    def add_money(self, amount):
        self.player.money += amount

    def spend_money(self, amount):
        if self.player.money >= amount:
            self.player.money -= amount
            return True
        return False