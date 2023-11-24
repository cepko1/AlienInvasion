import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Basic class for game"""

    def __init__(self):
        """Init game. Creation resourses"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        self.ship = Ship(self)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # move ship right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # move ship left
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _update_screen(self):
        # Renew background
        self.screen.fill(self.settings.bg_color)
        self._draw_sky()
        self.ship.blime()
        # Show screen
        pygame.display.flip()

    def _draw_sky(self):
        # draw sky with in top of screen
        pygame.draw.rect(self.screen, "blue", (0, 0, 1200, 100))

    def run_game(self):
        """Start main game"""
        while True:
            # Keyboard and mouse checking
            self._check_events()
            self.ship.update()
            self._update_screen()



if __name__ == "__main__":
    # Create and run game
    ai = AlienInvasion()
    ai.run_game()
