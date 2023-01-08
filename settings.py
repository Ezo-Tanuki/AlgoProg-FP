class Settings():
    def __init__(self) -> None:
        #window size
        self.screen_width = 600
        self.screen_height = 600

        #row and column for grid 
        self.columns = 3
        self.rows = 3

        #set cellsize
        self.preferred_cellsize = 100

        #set dot radius
        self.dot_radius = 5
        
        #set color
        self.bg_color = (255, 255, 255) #white
        self.dot_color = (0, 0, 0) #black

        #set button properties
        self.button_color = (200, 200, 200) #light gray
        self.text_color = (255, 255, 255) #white

        #Don't modify
        self.cellsize = min(self.preferred_cellsize, min(self.screen_width, self.screen_height) // (max(self.columns, self.rows) + 1))
        self.padding_x = (self.screen_width - self.rows * (self.cellsize)) // 2
        self.padding_y = (self.screen_height - self.columns * (self.cellsize)) // 2