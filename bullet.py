import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class for bullets management"""

    def __init__(self,ai_game):
        """Create bullet in the current ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Make bullet rect and move it for the correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # save bullet position as float
        self.y = float(self.rect.y)


    def update(self):
        """move bullet up"""
        # renew bullet position
        self.y -= self.settings.bullet_speed
        # renew rect position
        self.rect.y = self.y
        # if top of bullet is on top of screen the bullet is explod
        if self.y < 0:
            self.rect.width = self.settings.bullet_height
            self.color = (200, 0, 0)


    def draw_bullet(self):
        """Draw bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
