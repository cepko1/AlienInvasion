import sys

import pygame

class AlienInvasion:
    """Basic class for game"""

    def __init__(self):
        """Init game. Creation resourses"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,600))
        pygame.display.set_caption("Alien invasion")

    def run_game(self):
        """Start main game"""
        while True:
            # Keyboard and mouse checking
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Show screen
            pygame.display.flip()


if __name__ == "__main__":
    # Create and run game
    ai = AlienInvasion()
    ai.run_game()