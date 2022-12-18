import pygame

def update_screen(settings, screen, cells):
    
    screen.fill(settings.bg_color)
    draw_dot(settings, screen)
    updateCells(screen, cells)
    # test(screen, cells)

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

def updateCells(screen, cells):
    for cell in cells:
        cell.updateLines(screen)

def checkMultipleLineClick(cells, index, pos):
    collision = 0
    for line_object in cells[index].line_object:
        if line_object.collidepoint(pos):
            collision += 1;
        if collision > 1:
            return True
    
    return False


# def test(screen, cells):
#     for 
