class Settings():
    def __init__(self) -> None:
        self.screen_width = 600
        self.screen_height = 600

        self.columns = self.rows = 20
        
        self.cellsize = min(40, min(self.screen_width, self.screen_height) / (20-1))
        self.padding_x = (self.screen_width - self.rows * self.cellsize) / 2
        self.padding_y = (self.screen_width - self.rows * self.cellsize) / 2

        self.bg_color = (255, 255, 255) #white
        self.dot_color = (0, 0, 0) #black