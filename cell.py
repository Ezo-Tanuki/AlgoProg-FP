import pygame
from settings import Settings


class Cell():
    def __init__(self, row, column, s = Settings()):
        self.row = row
        self.column = column

        self.index = row * column + column
        self.rect = pygame.Rect(
            (s.padding_x + column*s.cellsize, s.padding_y + row*s.cellsize),
            (s.cellsize, s.cellsize)) #make a square object
        
        #stores top&bottom y coor. and left&right x coor. order = top right bottom left
        self.sides = (self.rect.top, self.rect.right, self.rect.bottom, self.rect.left) 
        
        self.corner = (
                    (self.sides[3], self.sides[0]), #top-left
                    (self.sides[1], self.sides[0]), #top-right
                    (self.sides[1], self.sides[2]), #bottom-right
                    (self.sides[3], self.sides[2])) #bottom-left
        
        self.line = [False] * 4 #up right down left
