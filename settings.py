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
        self.border = False

        # debug mode
        self.debug = False
