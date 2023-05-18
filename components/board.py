import pygame
from components.Pieces import Piece
from components.chess_pieces import *

LIGHT_GRAY = (180, 180, 180)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
class Board:
    def __init__(self, rows, cols, square_size):
        self.rows = rows
        self.cols = cols
        self.square_size = square_size
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]

    def create_pieces(self):
        raise NotImplementedError("create_pieces method must be implemented by the subclass")

    def draw(self, screen):
        raise NotImplementedError("draw method must be implemented by the subclass")

    def move_piece(self, piece, new_row, new_col):
        raise NotImplementedError("move_piece method must be implemented by the subclass")

    def is_valid_move(self, current_row, current_col, new_row, new_col):
        raise NotImplementedError("is_valid_move method must be implemented by the subclass")

class CheckersBoard(Board):
    def create_pieces(self):#populates board with checkers pieces
        for row in range(3):# places black pieces on board iterates 0,1,2
            for col in range(self.cols):
                if (row + col) % 2 == 0:
                    self.grid[row][col] = Piece(row, col, BLACK, self.square_size)

        for row in range(5, self.rows):#places white on board iterates from 5 to 7
            for col in range(self.cols):
                if (row + col) % 2 == 0:
                    self.grid[row][col] = Piece(row, col, WHITE,self.square_size)

    def draw(self, screen):#render board on the screen for checkers
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

    def is_valid_move(self, current_row, current_col, new_row, new_col):#validate moves for checkers
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

class ChessBoard(Board):
    def create_pieces(self):#populate board with chess pieces
        # Create black pieces
        self.grid[0][0] = Rook(row=0, col=0, color=BLACK, square_size=self.square_size)
        self.grid[0][1] = Knight(row=0, col=1, color=BLACK, square_size=self.square_size)
        self.grid[0][2] = Bishop(row=0, col=2, color=BLACK, square_size=self.square_size)
        self.grid[0][3] = Queen(row=0, col=3, color=BLACK, square_size=self.square_size)
        self.grid[0][4] = King(row=0, col=4, color=BLACK, square_size=self.square_size)
        self.grid[0][5] = Bishop(row=0, col=5, color=BLACK, square_size=self.square_size)
        self.grid[0][6] = Knight(row=0, col=6, color=BLACK, square_size=self.square_size)
        self.grid[0][7] = Rook(row=0, col=7, color=BLACK, square_size=self.square_size)
        for col in range(self.cols):
            self.grid[1][col] = Pawn(row=1, col=col, color=BLACK, square_size=self.square_size)

        # Create black pieces
        self.grid[7][0] = Rook(row=7, col=0, color=WHITE, square_size=self.square_size)
        self.grid[7][1] = Knight(row=7, col=1, color=WHITE, square_size=self.square_size)
        self.grid[7][2] = Bishop(row=7, col=2, color=WHITE, square_size=self.square_size)
        self.grid[7][3] = Queen(row=7, col=3, color=WHITE, square_size=self.square_size)
        self.grid[7][4] = King(row=7, col=4, color=WHITE, square_size=self.square_size)
        self.grid[7][5] = Bishop(row=7, col=5, color=WHITE, square_size=self.square_size)
        self.grid[7][6] = Knight(row=7, col=6, color=WHITE, square_size=self.square_size)
        self.grid[7][7] = Rook(row=7, col=7, color=WHITE, square_size=self.square_size)
        for col in range(self.cols):
            self.grid[6][col] = Pawn(row=6, col=col, color=WHITE, square_size=self.square_size)

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                if (row + col) % 2 == 0:
                    color = LIGHT_GRAY
                else:
                    color = DARK_GRAY

                pygame.draw.rect(screen, color, (col * self.square_size, row * self.square_size, self.square_size, self.square_size))

                piece = self.grid[row][col]
                if piece is not None:
                    piece.draw(screen)

    def move_piece(self, piece, new_row, new_col):
        current_row, current_col = piece.row, piece.col
        if self.is_valid_move(current_row, current_col, new_row, new_col):
            self.grid[current_row][current_col] = None
            self.grid[new_row][new_col] = piece
            piece.row = new_row
            piece.col = new_col


    def is_valid_move(self, current_row, current_col, new_row, new_col):#validate moves for chess
        piece = self.grid[current_row][current_col]
        color = piece.color

        if isinstance(piece, King):
            # Validate King's move
            if abs(new_row - current_row) <= 1 and abs(new_col - current_col) <= 1:
                return True

        elif isinstance(piece, Queen):
            # Validate Queen's move (diagonal, horizontal, or vertical)
            if new_row == current_row or new_col == current_col or abs(new_row - current_row) == abs(new_col - current_col):
                return True

        elif isinstance(piece, Rook):
            # Validate Rook's move (horizontal or vertical)
            if new_row == current_row or new_col == current_col:
                return True

        elif isinstance(piece, Bishop):
            # Validate Bishop's move (diagonal)
            if abs(new_row - current_row) == abs(new_col - current_col):
                return True

        elif isinstance(piece, Knight):
            # Validate Knight's move
            if (abs(new_row - current_row) == 2 and abs(new_col - current_col) == 1) or (abs(new_row - current_row) == 1 and abs(new_col - current_col) == 2):
                return True

        elif isinstance(piece, Pawn):
            # Validate Pawn's move
            if color == WHITE:
                # White pieces can move up one row and only to columns left or right from their position
                if new_row == current_row - 1 and abs(new_col - current_col) == 1:
                    return True
            elif color == BLACK:
                # Black pieces can move down one row and only to columns left or right from their position
                if new_row == current_row + 1 and abs(new_col - current_col) == 1:
                    return True

        return False
