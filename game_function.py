import pygame

def update_screen(settings, screen):
    
    screen.fill(settings.bg_color)
    draw_dot(settings, screen)

    pygame.display.flip()

def draw_dot(settings, screen):

    for row in range(settings.rows):
        for column in range(settings.columns):

            pygame.draw.circle(screen, settings.dot_color, (settings.padding_x + column*settings.cellsize, settings.padding_y + row*settings.cellsize), 2)