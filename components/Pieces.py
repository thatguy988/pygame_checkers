import pygame
King = (0, 0, 255)
class Piece:
    def __init__(self, row, col, color,square_size): # constructor that initializes the attributes of the Piece object. 
        self.row = row
        self.col = col
        self.color = color
        self.is_king = False
        self.square_size = square_size

    def draw(self,screen): # rendering the game piece on the screen takes screen has parameter
        radius = self.square_size // 2 - 10 #calculate radius of circle for piece #square_size//2 makes sure size of circle is smaller then square
        #subtract 10 to allow space between circle and square
        x = self.col * self.square_size + self.square_size // 2 #determine x position of center of circle
        y = self.row * self.square_size + self.square_size // 2 # deterne y position of center of circle
        pygame.draw.circle(screen, self.color, (x, y), radius) #draw piece has circle takes parameters from previous lines
        if self.is_king:
            pygame.draw.circle(screen, King, (x, y), radius // 2)
