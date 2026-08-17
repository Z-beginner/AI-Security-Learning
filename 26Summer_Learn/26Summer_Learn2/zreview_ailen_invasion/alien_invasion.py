import pygame
import sys
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()
            self.clock.tick(self.settings.fps)
if __name__ == "__main__":
    ai_game = AlienInvasion()
    ai_game.run_game()