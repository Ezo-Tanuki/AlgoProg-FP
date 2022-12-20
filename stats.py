import pygame
from settings import Settings

class Stats():
    def __init__(self, players, settings = Settings()):
        self.unclaimed_cells = settings.columns * settings.rows
        self.score = [0, 0] #player 1, player 2

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.game_active = False
