import pygame
import sys
import game_function as gf


from cell import Cell
from settings import Settings

def main():
    pygame.init()
    pygame.display.set_caption("Dot and Boxes")

    
    settings = Settings()
    cells = [Cell(row, column) for row in range(settings.rows) for column in range(settings.columns)] #render cell
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    run = True
    while run:
        gf.update_screen(settings, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                break

        
    

main()