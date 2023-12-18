import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class represent an alien"""
    def __init__(self,ai_game):
        """Init of alien and set its parameters"""
        super() .__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load image and set atributes
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Each new alien shows on the top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = self.rect.x

    def update(self) -> None:
        """Aliens movement"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self) -> bool:
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0:
            return True

