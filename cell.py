import pygame
from settings import Settings
from player import Player


class Cell():
    def __init__(self, row : int, column : int, screen : pygame.Surface, settings : Settings) -> None:
        self.row = row
        self.column = column

        self.screen = screen
        self.settings = settings

        self.index = row * column + column
        self.rect = pygame.Rect(
            self.settings.padding_x + column*self.settings.cellsize, self.settings.padding_y + row*self.settings.cellsize,
            self.settings.cellsize, self.settings.cellsize) #make a square object
        
        #stores top&bottom y coor. and left&right x coor. order = top right bottom left
        self.sides = (self.rect.top, self.rect.right, self.rect.bottom, self.rect.left) 
        
        self.corner = (
                    (self.sides[3], self.sides[0]), #top-left
                    (self.sides[1], self.sides[0]), #top-right
                    (self.sides[1], self.sides[2]), #bottom-right
                    (self.sides[3], self.sides[2])) #bottom-left
        
        self.line_object = (   
            pygame.Rect(self.rect.left + self.settings.dot_radius, self.rect.top - self.settings.dot_radius, self.settings.cellsize - self.settings.dot_radius * 2, self.settings.dot_radius * 2),
            pygame.Rect(self.rect.right - self.settings.dot_radius, self.rect.top + self.settings.dot_radius, self.settings.dot_radius * 2, self.settings.cellsize - self.settings.dot_radius * 2),
            pygame.Rect(self.rect.left + self.settings.dot_radius,self.rect.bottom - self.settings.dot_radius, self.settings.cellsize - self.settings.dot_radius * 2, self.settings.dot_radius * 2),
            pygame.Rect(self.rect.left - self.settings.dot_radius, self.rect.top + self.settings.dot_radius, self.settings.dot_radius * 2, self.settings.cellsize - self.settings.dot_radius * 2)
            ) #up right down left

        self.line = [None, None, None, None] #up right down left
        self.claim = None #
    
    def updateLines(self) -> None:
        for index, side in enumerate(self.line):
            if side != None:
                pygame.draw.line(self.screen, self.line[index], self.corner[index], self.corner[(index+1)% 4], 2)
            
            else:
                pygame.draw.line(self.screen, (210, 210, 210), self.corner[index], self.corner[(index+1)% 4], 2)
        #draw lines

    def displayLineObject(self) -> None:
        for side in self.line_object:
            if side != None:
                pygame.draw.rect(self.screen, (0, 0, 0), side) #display line object
    
    def checkClaimed(self, current_player : Player) -> bool:
        for line in self.line:
            if line == None:
                return False
            
        self.claim = current_player
        return True
    #return true if all line has a value

    def drawCell(self, cell_screen : pygame.display) -> None:
        if self.claim:
            pygame.draw.rect(cell_screen, self.claim.color, self.rect) #draw cell object
            
                
    def cellReset(self) -> None:
        self.line = [None, None, None, None]
        self.claim = None