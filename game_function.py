import pygame

def update_screen(settings, screen, cells):
    
    screen.fill(settings.bg_color)
    draw_dot(settings, screen)
    updateCells(screen, cells)

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
        if line.collidepoint(pos):
            return index
    
    return -1

def updateCells(screen, cells):
    for cell in cells:
        # cell.updateLines(screen)
        cell.displayLineObject(screen)
    
    return None

def checkLineSelected(cells, pos, players, current_player):
    triggered = False
    for cell in cells:
        index = checkLineObjectTriggered(cell, pos)
        if index != -1:
            triggered = True
            print("y")
            cell.line[index] == current_player[0].color
    
    if triggered:
        current_player[0] = players[(current_player[1]+1)%len(players)]
        current_player[1] += 1


def checkEvents(settings, screen, cells, players, current_player):

    for event in pygame.event.get():
            if event.type == pygame.QUIT: #close window if 'x' is clicked
                pygame.quit()
                break

            if event.type == pygame.MOUSEBUTTONDOWN: #save mouse position in an event of mouse click
                mousePos = event.pos
                checkLineSelected(cells, mousePos, players, current_player)

                showTriggeredCell(cells, mousePos)
