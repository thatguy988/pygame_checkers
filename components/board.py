import pygame
from components.Pieces import Piece
# Define colors
LIGHT_GRAY = (180, 180, 180)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
class Board:
    def __init__(self,rows,cols,square_size):
        self.rows=rows
        self.cols=cols
        self.square_size=square_size
        self.grid = [[None] * cols for _ in range(rows)]

    def create_pieces(self):
        for row in range(3):
            for col in range(self.cols):
                if (row + col) % 2 == 0:
                    self.grid[row][col] = Piece(row, col, BLACK, self.square_size)

        for row in range(5, self.rows):
            for col in range(self.cols):
                if (row + col) % 2 == 0:
                    self.grid[row][col] = Piece(row, col, WHITE,self.square_size)

    def draw(self, screen):
        screen.fill(LIGHT_GRAY)
        for row in range(self.rows):
            for col in range(row % 2, self.cols, 2):
                pygame.draw.rect(screen, DARK_GRAY, (col * self.square_size, row * self.square_size, self.square_size, self.square_size))
                piece = self.grid[row][col]
                if piece:
                    piece.draw(screen)
