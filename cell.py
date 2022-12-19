import pygame
from settings import Settings


class Cell():
    def __init__(self, row, column, s = Settings()):
        self.row = row
        self.column = column

        self.index = row * column + column
        self.rect = pygame.Rect(
            s.padding_x + column*s.cellsize, s.padding_y + row*s.cellsize,
            s.cellsize, s.cellsize) #make a square object
        
        #stores top&bottom y coor. and left&right x coor. order = top right bottom left
        self.sides = (self.rect.top, self.rect.right, self.rect.bottom, self.rect.left) 
        
        self.corner = (
                    (self.sides[3], self.sides[0]), #top-left
                    (self.sides[1], self.sides[0]), #top-right
                    (self.sides[1], self.sides[2]), #bottom-right
                    (self.sides[3], self.sides[2])) #bottom-left
        
        self.line_object = [   
            pygame.Rect(self.rect.left + s.dot_radius, self.rect.top - s.dot_radius, s.cellsize - s.dot_radius * 2, s.dot_radius * 2),
            pygame.Rect(self.rect.right - s.dot_radius, self.rect.top + s.dot_radius, s.dot_radius * 2, s.cellsize - s.dot_radius * 2),
            pygame.Rect(self.rect.left + s.dot_radius,self.rect.bottom - s.dot_radius, s.cellsize - s.dot_radius * 2, s.dot_radius * 2),
            pygame.Rect(self.rect.left - s.dot_radius, self.rect.top + s.dot_radius, s.dot_radius * 2, s.cellsize - s.dot_radius * 2)
            ] #up right down left

        self.line = [False, False, False, False] #up right down left
        self.claim = None #
    
    def updateLines(self, screen):
        for index, side in enumerate(self.line):
            if side:
                pygame.draw.line(screen, self.line[index], self.corner[index], self.corner[(index+1)% 4], 2)

    def displayLineObject(self, screen):
        for side in self.line_object:
            if side:
                pygame.draw.rect(screen, (0, 0, 0), side)
    
    def checkClaimed(self, current_player):
        for line in self.line:
            if not line:
                return
            
        self.claim = current_player

    def drawCell(self, screen):
        if self.claim:
            pygame.draw.rect(screen, self.claim[0].color, self.rect)
                
