import pygame
from systems.game import Game
from systems.chess_game import ChessGame

def main():
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Game Selector")

    font = pygame.font.Font(None, 36)

    game_options = ["Checkers", "Chess", "Quit"]
    selected_option = None

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                for i, option in enumerate(game_options):
                    option_rect = pygame.Rect(100, 200 + i * 50, 200, 40)
                    if option_rect.collidepoint(mouse_pos):
                        selected_option = option

        screen.fill((255, 255, 255))

        for i, option in enumerate(game_options): # draw on screen select options
            option_rect = pygame.Rect(100, 200 + i * 50, 200, 40)
            pygame.draw.rect(screen, (200, 200, 200), option_rect)
            text = font.render(option, True, (0, 0, 0))
            text_rect = text.get_rect(center=option_rect.center)
            screen.blit(text, text_rect)

        pygame.display.flip()

        # Check if an option is selected
        if selected_option is not None:
            if selected_option == "Checkers":
                checkers_game = Game()
                checkers_game.run()
            elif selected_option == "Chess":
                chess_game = ChessGame()
                chess_game.run()
            elif selected_option == "Quit":
                pass
            break

    
    pygame.quit()

if __name__ == "__main__":
    main()


