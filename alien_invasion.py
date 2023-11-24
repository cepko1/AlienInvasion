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
        self.event = pygame.event.get()
        if self.settings.fullscreen:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        self.ship = Ship(self)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        if self.settings.debug:
            self.event = event.key
            self._draw_text(event.key)

        if event.key == pygame.K_RIGHT:
            # move ship right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # move ship left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # Renew background
        self.screen.fill(self.settings.bg_color)
        self._draw_sky()
        self.ship.blime()
        if self.settings.debug:
            self._draw_text(self.event)
        # Show screen
        pygame.display.flip()

    def _draw_text(self, event):
        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render(str(self.event), True, (200, 0, 0))
        print(self.event)
        # self.screen.blit(text_surface, (200, 200))
        self.screen.blit(text_surface, (self.settings.screen_width // 2, self.settings.screen_height //2))

    def _draw_sky(self):
        # draw sky with in top of screen
        pygame.draw.rect(self.screen, "blue", (0, 0, self.settings.screen_width, 100))

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
