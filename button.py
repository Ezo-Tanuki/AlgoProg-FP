import pygame
from settings import Settings

class Button():
    def __init__(self, screen : pygame.Surface, msg : str, settings : Settings) -> None:
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        self.width, self.height = 200, 50
        self.button_color = settings.button_color
        self.text_color = settings.text_color
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prepMsg(msg)
    
    def prepMsg(self, msg : str) -> None:
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def drawButton(self) -> None:
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)