import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Basic class for game"""

    def __init__(self):
        """Init game. Creation resourses"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)


    def run_game(self):
        """Start main game"""
        while True:
            # Keyboard and mouse checking
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Renew background
            self.screen.fill(self.settings.bg_color)
            # Show screen
            pygame.display.flip()


if __name__ == "__main__":
    # Create and run game
    ai = AlienInvasion()
    ai.run_game()