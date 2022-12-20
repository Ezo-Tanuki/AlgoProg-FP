import pygame
import sys

def update_screen(settings, screen, cells):
    
    screen.fill(settings.bg_color)
    updateCells(screen, cells)
    draw_dot(settings, screen)
    pygame.display.flip()

def draw_dot(settings, screen):

    for row in range(settings.rows+1):
        for column in range(settings.columns+1):

            pygame.draw.circle(screen, settings.dot_color, 
                (settings.padding_x + column*settings.cellsize, settings.padding_y + row*settings.cellsize), settings.dot_radius)
            
def showTriggeredCell(cells, pos):
    for cell in cells:
        if pos and cell.rect.collidepoint(pos):
            print(cell.rect)

def checkLineObjectTriggered(cell, pos):
    for index, line in enumerate(cell.line_object):
        #checks whether the line object in the cell object is clicked and is triggered before
        if line.collidepoint(pos) and not cell.line[index]: 
            return index
    
    return -1

def updateCells(screen, cells):
    for cell in cells:
        cell.drawCell(screen)
        cell.updateLines(screen)
    
    return None

def checkLineSelected(cells, pos, players, current_player):
    #checks line object for each cell is successfully clicked if so change the current player and put the line
    triggered = False
    for cell in cells:
        index = checkLineObjectTriggered(cell, pos)

        if index != -1:
            triggered = True
            print("Line triggered!")
            cell.line[index] = current_player[0].color

            if cell.checkClaimed(current_player[0]):
                current_player[0].score += 1
        
    
    #switch player
    if triggered:
        current_player[0] = players[(current_player[1]+1)%len(players)]
        current_player[1] += 1


def checkEvents(settings, screen, cells, players, current_player, stats):

    for event in pygame.event.get():
            if event.type == pygame.QUIT: #close window and program if 'x' is clicked
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN: #save mouse position in an event of mouse click
                mousePos = event.pos
                checkLineSelected(cells, mousePos, players, current_player)

                showTriggeredCell(cells, mousePos)
