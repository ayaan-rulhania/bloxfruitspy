# pirate_game_loop.py
import pygame as pg
import random
from .settings import *
from .player.player import Player
from .enemy.bandit import Bandit
from .enemy.pirate import Pirate
from .world.pirate_village import PirateVillage

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font('arial')
        self.enemy_spawn_timer = 0
        self.current_world = None

    def new(self):
        """Start a new game."""
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.enemies = pg.sprite.Group()
        self.fruits = pg.sprite.Group()

        # Initialize Player and World
        self.player = Player(self, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.current_world = PirateVillage(self)

        # Initial Enemy Spawn
        self.spawn_enemy(Bandit, 50, 50)

        self.run()

    def spawn_enemy(self, enemy_class, x, y):
        """Helper to spawn an enemy instance."""
        enemy_class(self, x, y)

    def run(self):
        """Main game loop."""
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000 # Delta time in seconds
            self.events()
            self.update()
            self.draw()

    def events(self):
        """Handle all events (input)."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit_game()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit_game()
                # Placeholder for Attack
                if event.key == pg.K_SPACE:
                    print("Attack initiated (Need to implement in attacks.py)")

    def update(self):
        """Update game state and check for collisions."""
        self.all_sprites.update()

        # 1. Enemy Spawning Logic
        self.enemy_spawn_timer += 1
        if self.enemy_spawn_timer > ENEMY_SPAWN_RATE:
            # Spawn a random enemy at a random corner
            x = random.choice([0, SCREEN_WIDTH])
            y = random.choice([0, SCREEN_HEIGHT])
            self.spawn_enemy(random.choice([Bandit, Pirate]), x, y)
            self.enemy_spawn_timer = 0

        # 2. Player-Enemy Collision (Player takes damage)
        hits = pg.sprite.spritecollide(self.player, self.enemies, False)
        if hits:
            self.player.health -= 1 # Small damage per frame of collision
            if self.player.health <= 0:
                print("GAME OVER")
                self.playing = False

    def draw_text(self, surface, text, size, x, y, color=WHITE):
        """Helper function to draw text on the screen."""
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surface.blit(text_surface, text_rect)

    def draw(self):
        """Draw everything to the screen."""
        self.screen.fill(BLACK)

        # Draw the current world map/background
        if self.current_world:
            self.current_world.draw_map(self.screen)

        self.all_sprites.draw(self.screen)

        # Draw HUD (Health, Money)
        self.draw_text(self.screen, f"Health: {self.player.health}", 24, 80, 10, RED)
        self.draw_text(self.screen, f"Money: ${self.player.money}", 24, 80, 40, YELLOW)

        pg.display.flip()

    def quit_game(self):
        self.playing = False
        self.running = False