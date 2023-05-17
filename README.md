Pygame Checkers Documentation


Introduction:
The Pygame Checkers program is a simple implementation of the traditional checkers game using the Pygame library. It is an 8x8 checkerboard. The game supports mouse input for selecting and dragging game pieces.

Project Structure:
The program consists of the following files and classes:
main.py: This is the entry point of the program. It initializes the game and starts the game loop.
To run the Pygame Checkers program, execute the following command in the terminal: python main.py
systems/game.py: Contains the `Game` class that manages the game logic.
The game class is responsible for managing the game logic, including the game loop and handling user input. Game class has methods for initializing the game, running the game loop, and handling mouse input.
components/board.py: Contains the `Board` class that represents the game board.
The board represents the game board and contains the grid of game pieces. The board class has methods for creating the initial game setup and drawing the board and pieces on the screen.
components/pieces.py: Contains the `Piece` class that represents a game piece.
A Piece represent a game piece on board. Its attributes are its position, color, and king piece.Piece class has method for drawing piece on the screen 

Game Controls
- Left Mouse Button:
  - Clicking on a game piece selects it.
  - Holding and dragging a selected game piece allows you to move it to a valid position.
  - Releasing the mouse button drops the selected game piece.
  
The program relies on the following dependencies:
- Python 3.11.3
- Pygame 2.3.0












