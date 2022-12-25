import pygame
from settings import Settings

class Stats():
    def __init__(self, screen, players, settings = Settings()):
        self.unclaimed_cells = settings.columns * settings.rows
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        self.text_color = [(255, 177, 177), (177, 177, 255)]
        self.font = pygame.font.SysFont(None, 48)

        self.game_active = False
        self.prepScore(players)

    def prepScore(self, players):
        score = [player.score for player in players]
        score_str = list(map(str, score))
        self.score_images = [
            self.font.render(score_str[0], True, self.text_color[0],self.settings.bg_color),
            self.font.render(score_str[1], True, self.text_color[1], self.settings.bg_color)]
        
        self.score_rects = [image.get_rect() for image in self.score_images]
        self.score_rects[0].left = self.screen_rect.left + 20
        self.score_rects[0].top = 20
        self.score_rects[1].right = self.screen_rect.right - 20
        self.score_rects[1].top = 20
    
    def showScore(self):
        for image, score in zip(self.score_images, self.score_rects):
            self.screen.blit(image, score)