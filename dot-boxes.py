import pygame
import sys
import game_function as gf


from cell import Cell
from settings import Settings

def main():
    pygame.init()
    pygame.display.set_caption("Dot and Boxes")

    
    settings = Settings()
    cells = [Cell(row, column) for row in range(settings.rows)
        for column in range(settings.columns)] #render cell object
    
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    run = True
    print(cells[0].rect)
    while run:
        gf.update_screen(settings, screen, cells)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #close window if 'x' is clicked
                pygame.quit()
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN: #save mouse position in an event of mouse click
                mousePos = event.pos
                gf.showTriggeredCell(cells, mousePos)

        
    

main()