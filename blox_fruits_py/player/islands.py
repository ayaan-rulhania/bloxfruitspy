# player/islands.py

class IslandMap:
    """Manages the world map, island discovery, and travel."""
    def __init__(self, game):
        self.game = game
        self.unlocked_islands = ["Pirate Village"]
        self.current_island = "Pirate Village"

    def travel_to(self, island_name):
        if island_name in self.unlocked_islands:
            self.current_island = island_name
            print(f"Traveling to {island_name}...")
            return True
        return False