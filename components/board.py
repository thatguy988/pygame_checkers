import pygame
from components.Pieces import Piece
LIGHT_GRAY = (180, 180, 180)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
class Board:
    def __init__(self,rows,cols,square_size): #assign board object with attributes for rows, cols, squaresize
        self.rows=rows
        self.cols=cols
        self.square_size=square_size
        self.grid = [[None] * cols for _ in range(rows)]#2d list

    def create_pieces(self):#populates board with checkers pieces
        for row in range(3):# places black pieces on board iterates 0,1,2
            for col in range(self.cols):
                if (row + col) % 2 == 0:
                    self.grid[row][col] = Piece(row, col, BLACK, self.square_size)

        for row in range(5, self.rows):#places white on board iterates from 5 to 7
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


    def move_piece(self, piece, new_row, new_col):
        current_row, current_col = piece.row, piece.col
        if self.is_valid_move(current_row, current_col, new_row, new_col):
            self.grid[current_row][current_col] = None
            self.grid[new_row][new_col] = piece
            piece.row = new_row
            piece.col = new_col

    def is_valid_move(self, current_row, current_col, new_row, new_col):
        piece = self.grid[current_row][current_col]
        color = piece.color
        if color == WHITE:
            # White pieces can move up one row and only to columns left or right from their position
            if new_row == current_row - 1 and abs(new_col - current_col) == 1:
                return True
        elif color == BLACK:
            # Black pieces can move down one row and only to columns left or right from their position
            if new_row == current_row + 1 and abs(new_col - current_col) == 1:
                return True

        return False
