class Settings:
    """Class for saving game's settings"""

    def __init__(self):
        """Init game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.caption = "Alien invasion"
        self.fullscreen = False
        # ship settings
        self.ship_speed = 1.5
        self.border = True  # is screen border hard

        # bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Alien movement settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # 1 = rigth -1 = left

        # debug mode
        self.debug = False
