import pygame

class ChessPieces:
    def __init__(self, row, col, color, square_size):
        self.row = row
        self.col = col
        self.color = color
        self.square_size = square_size

    def draw(self, screen):
        raise NotImplementedError("draw method must be implemented in derived classes")

class King(ChessPieces):
    def draw(self, screen):
        x = self.col * self.square_size + self.square_size // 2
        y = self.row * self.square_size + self.square_size // 2

        # Draw the body of the king
        pygame.draw.rect(screen, self.color, (x - 20, y - 30, 40, 60))

        # Draw the crown on top of the king
        crown_points = [(x - 20, y - 30), (x, y - 60), (x + 20, y - 30)]
        pygame.draw.polygon(screen, self.color, crown_points)
        

class Queen(ChessPieces):
    def draw(self, screen):
        x = self.col * self.square_size + self.square_size // 2
        y = self.row * self.square_size + self.square_size // 2

        # Draw the body of the queen
        pygame.draw.circle(screen, self.color, (x, y), 30)

        # Draw the crown on top of the queen
        pygame.draw.polygon(screen, self.color, [(x - 20, y - 30), (x, y - 60), (x + 20, y - 30)])
        

class Rook(ChessPieces):
    def draw(self, screen):
        radius = self.square_size // 2 - 10
        x = self.col * self.square_size + self.square_size // 2
        y = self.row * self.square_size + self.square_size // 2

        pygame.draw.circle(screen, self.color, (x, y), radius)

        # Draw the rook shape
        rook_width = self.square_size // 2 - 10
        rook_height = self.square_size // 2 - 10

        rook_rect = pygame.Rect(x - rook_width // 2, y - rook_height // 2, rook_width, rook_height)
        pygame.draw.rect(screen, self.color, rook_rect)
        

class Bishop(ChessPieces):
    def draw(self, screen):
        radius = self.square_size // 2 - 10
        x = self.col * self.square_size + self.square_size // 2
        y = self.row * self.square_size + self.square_size // 2

        pygame.draw.circle(screen, self.color, (x, y), radius)

        # Draw the bishop shape
        bishop_size = self.square_size // 2 - 10

        bishop_rect = pygame.Rect(x - bishop_size // 2, y - bishop_size // 2, bishop_size, bishop_size)
        pygame.draw.rect(screen, self.color, bishop_rect)
        pygame.draw.line(screen, self.color, (x, y - bishop_size // 2), (x - bishop_size // 2, y), 5)
        pygame.draw.line(screen, self.color, (x, y - bishop_size // 2), (x + bishop_size // 2, y), 5)
        pygame.draw.line(screen, self.color, (x, y + bishop_size // 2), (x - bishop_size // 2, y), 5)
        pygame.draw.line(screen, self.color, (x, y + bishop_size // 2), (x + bishop_size // 2, y), 5)

class Knight(ChessPieces):
    def draw(self, screen):
        radius = self.square_size // 2 - 10
        x = self.col * self.square_size + self.square_size // 2
        y = self.row * self.square_size + self.square_size // 2

        pygame.draw.circle(screen, self.color, (x, y), radius)

        # Draw the knight shape
        knight_size = self.square_size // 2 - 10

        knight_points = [
            (x - knight_size // 2, y - knight_size // 2),
            (x + knight_size // 2, y - knight_size // 2),
            (x + knight_size // 2, y + knight_size // 4),
            (x + knight_size // 4, y + knight_size // 2),
            (x - knight_size // 4, y + knight_size // 2),
            (x - knight_size // 2, y + knight_size // 4)
        ]

        pygame.draw.polygon(screen, self.color, knight_points)

class Pawn(ChessPieces):
    def draw(self, screen):
        radius = self.square_size // 2 - 10
        x = self.col * self.square_size + self.square_size // 2
        y = self.row * self.square_size + self.square_size // 2

        pygame.draw.circle(screen, self.color, (x, y), radius)

        # Draw the pawn shape
        pawn_size = self.square_size // 2 - 10

        pawn_points = [
            (x - pawn_size // 2, y + pawn_size // 2),
            (x + pawn_size // 2, y + pawn_size // 2),
            (x + pawn_size // 2, y - pawn_size // 2),
            (x - pawn_size // 4, y - pawn_size // 2),
            (x - pawn_size // 2, y - pawn_size // 4),
            (x - pawn_size // 2, y + pawn_size // 2)
        ]

        pygame.draw.polygon(screen, self.color, pawn_points)
