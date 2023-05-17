import pygame
import sys
from components.board import Board
WIDTH,HEIGHT=800,800
rows,cols=8,8
class Game:
    def __init__(self):
        square_size = WIDTH//cols
        self.board = Board(rows,cols,square_size)
        self.board.create_pieces()
        self.dragging_piece = None

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        mouse_pos = pygame.mouse.get_pos()
                        clicked_row = mouse_pos[1] // self.board.square_size
                        clicked_col = mouse_pos[0] // self.board.square_size
                        self.dragging_piece = self.board.grid[clicked_row][clicked_col]

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  # Left mouse button
                        self.dragging_piece = None

                if event.type == pygame.MOUSEMOTION:
                    if self.dragging_piece is not None:
                        mouse_pos = pygame.mouse.get_pos()
                        self.dragging_piece.row = mouse_pos[1] // self.board.square_size
                        self.dragging_piece.col = mouse_pos[0] // self.board.square_size


            self.board.draw(screen)

            pygame.display.update()
            clock.tick(60)
