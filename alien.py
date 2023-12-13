import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class represent an alien"""
    def __init__(self,ai_game):
        """Init of alien and set its parameters"""
        super() .__init__()
        self.screen = ai_game.screen

        #Load image and set atributes
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Each new alien shows on the top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = self.rect.x
