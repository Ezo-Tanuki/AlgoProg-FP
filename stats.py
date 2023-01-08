import pygame
from settings import Settings
from player import Player

class Stats():
    def __init__(self, screen : pygame.Surface, players : list[Player], settings : Settings) -> None:
        self.total_grid = settings.columns * settings.rows
        self.unclaimed_cells = self.total_grid
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.winner = None
        self.players = players

        self.text_color = [(255, 177, 177), (177, 177, 255)]
        self.font = pygame.font.SysFont(None, 48)

        self.game_active = True
        self.prepScore()

    def prepScore(self) -> None:
        score = [player.score for player in self.players]
        score_str = list(map(str, score))
        self.score_images = [
            self.font.render(score_str[0], True, self.text_color[0],self.settings.bg_color),
            self.font.render(score_str[1], True, self.text_color[1], self.settings.bg_color)]
        
        self.score_rects = [image.get_rect() for image in self.score_images]
        self.score_rects[0].left = self.screen_rect.left + 20
        self.score_rects[0].top = 20
        self.score_rects[1].right = self.screen_rect.right - 20
        self.score_rects[1].top = 20
    
    def showScore(self) -> None:
        for image, score in zip(self.score_images, self.score_rects):
            self.screen.blit(image, score)

    def setWinner(self) -> None:
        if self.players[0].score > self.players[1].score:
            self.winner = self.players[0]
            return
        
        if self.players[0].score < self.players[1].score:
            self.winner = self.players[1]

    def showWinner(self) -> None:
        if self.winner is self.players[0]:
            idx = 0
            winner_str = "Player 1 win"
        
        elif self.winner is self.players[1]:
            idx = 1
            winner_str = "Player 2 win"
        
        else:
            idx = None
            winner_str = "Draw"


        if idx != None:
            image = self.font.render(winner_str, True, self.players[idx].color, self.settings.bg_color)
        
        image = self.font.render(winner_str, True, (200, 200, 200), self.settings.bg_color)
        image_rect = image.get_rect()
        image_rect.top = 40
        image_rect.centerx = self.screen.get_width() / 2
        self.screen.blit(image, image_rect)

    def resetStats(self) -> None:
        self.unclaimed_cells = self.total_grid
        self.game_active = True
        self.winner = None