import pygame
import sys
from components.board import CheckersBoard

WIDTH, HEIGHT = 800, 800
rows, cols = 8, 8

class Game:
    def __init__(self):
        square_size = WIDTH // cols
        self.board = CheckersBoard(rows, cols, square_size) 
        self.board.create_pieces()
        self.selected_piece = None
        self.dragging = False

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Checkers")

        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button pressed
                        mouse_pos = pygame.mouse.get_pos()
                        clicked_row = mouse_pos[1] // self.board.square_size
                        clicked_col = mouse_pos[0] // self.board.square_size
                        self.selected_piece = self.board.grid[clicked_row][clicked_col]
                        if self.selected_piece is not None:
                            self.dragging = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  # Left mouse button released
                        if self.dragging and self.selected_piece is not None:
                            mouse_pos = pygame.mouse.get_pos()
                            new_row = mouse_pos[1] // self.board.square_size
                            new_col = mouse_pos[0] // self.board.square_size
                            self.board.move_piece(self.selected_piece, new_row, new_col)
                        self.selected_piece = None
                        self.dragging = False

            self.board.draw(screen)

            pygame.display.update()
            clock.tick(60)
