import pygame

class Ship:
    """Ship management class"""

    def __init__(self, ai_game):
        """Init ship and give start position for it"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and give its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Every new ship appear in the center of screen bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # save decimal value of ship position
        self.x = float(self.rect.x)

        # indicating of movement
        self.moving_right = False
        self.moving_left = False

    def blime(self):
        """Draw ship in its current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """update ship position by indication of movement"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left >0:
            self.x -= self.settings.ship_speed

        #update ship object
        self.rect.x = self.x


