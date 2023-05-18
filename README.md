Pygame Checkers Documentation


Introduction:
The Pygame Checkers and Chess program is a simple implementation of the traditional checkers and chess games using the Pygame library. It is an 8x8 checkerboard. The game supports mouse input for selecting and dragging game pieces.

Project Structure:

The program consists of the following files and classes:

checkers.py: This is the entry point of the program. User chooses between checkers and chess. It initializes the game and starts the game loop.

systems/game.py: Contains the `Game` class that manages the checkers game logic.

The game class is responsible for managing the game logic, including the game loop and handling user input. Game class has methods for initializing the game, running the game loop, and handling mouse input.

systems/chess_game.py: Contains the `ChessGame` class that manages the chess game logic.

The ChessGame class is responsible for managing the game logic, including the game loop and handling user input. Game class has methods for initializing the game, running the game loop, and handling mouse input.

components/board.py: Contains the `Board` class that represents the game board.

The board represents the game board and contains the grid of game pieces. The board subclasses checkersboard and chessboard each has four methods for creating the pieces for game, rendering pieces on board, move pieces, and validate the moves.

components/pieces.py: Contains the `Piece` class that represents a game piece.

A Piece represent a game piece on board. Its attributes are its position, color, and king piece.Piece class has method for drawing piece on the screen 

components/chess_pieces.py: Contains the 'Piece' class that represents a piece in chess game. 

The six different chess pieces inherit the attributes of piece class with each having their own method for how the piece is render on screen.


Game Controls
- Left Mouse Button:
  - Clicking on a game piece selects it.
  - Holding and dragging a selected game piece allows you to move it to a valid position.
  - Releasing the mouse button drops the selected game piece.
  
The program relies on the following dependencies:
- Python 3.11.3
- Pygame 2.3.0












