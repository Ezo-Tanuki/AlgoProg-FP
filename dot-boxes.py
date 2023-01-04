import pygame
import sys
import game_function as gf

from player import Player
from cell import Cell
from settings import Settings
from stats import Stats
from button import Button

RED = (255, 0, 0)
BLUE = (0, 0, 255)

def main():
    pygame.init()
    pygame.display.set_caption("Dot and Boxes")
    
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    
    
    
    cells = [Cell(row, column, screen, settings) for row in range(settings.rows)
        for column in range(settings.columns)] #render cell object
    players = (Player(RED), Player(BLUE))
    
    current_player = [players[0], 0]
    
    stats = Stats(screen, players, settings)
    button = Button(screen, "Retry", settings)
    run = True
    while run:
        gf.update_screen(settings, screen, cells, players, stats, button)
        gf.checkEvents(settings, screen, cells, players, current_player, stats, button)
        
        
        
if __name__ == "__main__":
    main()