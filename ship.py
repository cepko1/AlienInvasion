import pygame

class Ship:
    """Ship management class"""

    def __init__(self, ai_game):
        """Init ship and give start position for it"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and give its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Every new ship appear in the center of screen bottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blime(self):
        """Draw ship in its current position"""
        self.screen.blit(self.image, self.rect)

