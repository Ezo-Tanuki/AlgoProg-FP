import pygame
import sys

def update_screen(settings, screen, grid, players, stats, button):
    
    screen.fill(settings.bg_color) #background color

    cell_screen = pygame.Surface((screen.get_width(), screen.get_height()))
    cell_screen.fill((255, 255, 255))
    cell_screen.set_colorkey((255, 255, 255))
    cell_screen.set_alpha(100)
    updateCells(grid, cell_screen) #update all cell
    
    screen.blit(cell_screen, (0, 0))

    draw_dot(settings, screen) #draw dots
    stats.prepScore() #render score
    stats.showScore() #show score
    if not stats.game_active: #show button if game is not active
        button.drawButton()
        stats.showWinner()

    pygame.display.update() #refresh screen

def draw_dot(settings, screen):

    for row in range(settings.rows+1):
        for column in range(settings.columns+1):

            pygame.draw.circle(screen, settings.dot_color, 
                (settings.padding_x + column*settings.cellsize, settings.padding_y + row*settings.cellsize), settings.dot_radius)
            
def showTriggeredCell(grid, pos):
    for cell in grid:
        if pos and cell.rect.collidepoint(pos):
            print(cell.rect)

def checkLineObjectTriggered(cell, pos):
    for index, line in enumerate(cell.line_object):
        #checks whether the line object in the cell object is clicked and is has not been triggered before
        if line.collidepoint(pos) and not cell.line[index]: 
            return index
    
    return -1

def updateCells(grid, cell_screen):
    for cell in grid:
        cell.drawCell(cell_screen) #draw all cell object
        cell.updateLines() #draw line
    
    return None

def checkLineSelected(grid, pos, players, current_player, stats):
    #checks line object for each cell is successfully clicked if so change the current player and put the line
    triggered = False
    for cell in grid:
        index = checkLineObjectTriggered(cell, pos) 
        '''
        check for any line object triggered and return an index from 
        0-3 (signifying the sides from top, right, bottom, left respectively) 
        if the line object has not been triggered, otherwise return -1
        '''
        if index != -1:
            triggered = True
            print("Line triggered!")
            cell.line[index] = current_player[0].color
            #save the player color as the line color

            if cell.checkClaimed(current_player[0]):
                current_player[0].score += 1 #add score to the current player
                stats.unclaimed_cells -= 1 #reduce unclaimed cell by 1

    #switch player
    if triggered:
        current_player[0] = players[(current_player[1]+1)%len(players)]
        current_player[1] += 1

def checkButtonClicked(button, mousePos):
    return button.rect.collidepoint(mousePos)

def checkEvents(settings, screen, grid, players, current_player, stats, button):

    for event in pygame.event.get(): #lists all event
            if event.type == pygame.QUIT: #close window and program if 'x' is clicked
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN: #save mouse position in an event of mouse click
                mousePos = event.pos
                if stats.game_active: #if game in active status start the game
                    checkLineSelected(grid, mousePos, players, current_player, stats)

                    showTriggeredCell(grid, mousePos)

                    if stats.unclaimed_cells <= 0:
                        stats.game_active = False
                        stats.setWinner()
                
                else: #otherwise the game will wait the play button to be clicked
                    if checkButtonClicked(button, mousePos):
                        gameReset(grid, players, stats)

def gameReset(grid, players, stats):
    for cell in grid:
        cell.cellReset()
    for player in players:
        player.resetScore()

    stats.resetStats()
