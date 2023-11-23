class Settings:
    """Class for saving game's settings"""

    def __init__(self):
        """Init game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.caption = "Alien invasion"