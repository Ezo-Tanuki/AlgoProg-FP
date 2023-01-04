class Settings():
    def __init__(self) -> None:
        self.screen_width = 600
        self.screen_height = 600

        self.columns = self.rows = 10
        
        self.cellsize = min(100, min(self.screen_width, self.screen_height) // (self.columns+1))
        self.padding_x = (self.screen_width - self.rows * (self.cellsize)) // 2
        self.padding_y = (self.screen_width - self.columns * (self.cellsize)) // 2

        self.dot_radius = 5
        
        self.bg_color = (255, 255, 255) #white
        self.dot_color = (0, 0, 0) #black