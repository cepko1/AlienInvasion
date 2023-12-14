import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create new bullet and add it to group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Create fleet of aliens"""
        #Create aliens and determinate amount of them in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # determinate how many rows can show on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #create first row of the aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                # Create an alien and add it to the row
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        # Renew background
        self.screen.fill(self.settings.bg_color)
        # self._draw_sky()
        self.ship.blime()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
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

    def _update_bullets(self):
        """Renew bullets position and delete excessive bullets"""
        self.bullets.update()
        # Delete bullets which out the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def run_game(self):
        """Start main game"""
        while True:
            # Keyboard and mouse checking
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()




if __name__ == "__main__":
    # Create and run game
    ai = AlienInvasion()
    ai.run_game()
