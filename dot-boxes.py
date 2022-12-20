import pygame
import sys
import game_function as gf

from player import Player
from cell import Cell
from settings import Settings
from stats import Stats

def main():
    pygame.init()
    pygame.display.set_caption("Dot and Boxes")

    
    settings = Settings()
    
    cells = [Cell(row, column) for row in range(settings.rows)
        for column in range(settings.columns)] #render cell object
    players = (Player((255, 0, 0)), Player((0, 0, 255)))
    stats = Stats(players)
    current_player = [players[0], 0]
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    run = True
    print(cells[0].rect)
    while run:
        gf.update_screen(settings, screen, cells)
        gf.checkEvents(settings, screen, cells, players, current_player, stats)
        
        
        
if __name__ == "__main__":
    main()