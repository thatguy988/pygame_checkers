import pygame
WHITE = (255, 255, 255)
class Piece:
    def __init__(self, row, col, color,square_size):
        self.row = row
        self.col = col
        self.color = color
        self.is_king = False
        self.square_size = square_size

    def draw(self,screen):
        radius = self.square_size // 2 - 10
        x = self.col * self.square_size + self.square_size // 2
        y = self.row * self.square_size + self.square_size // 2
        pygame.draw.circle(screen, self.color, (x, y), radius)
        if self.is_king:
            pygame.draw.circle(screen, WHITE, (x, y), radius // 2)
