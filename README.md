# 2048 Game

This is a simple implementation of the 2048 game using Pygame. The game involves sliding numbered tiles on a grid to combine them to create a tile with the number 2048.

## Features

- **Slide Tiles**: Move tiles in four directions (left, right, up, down).
- **Combine Tiles**: Combine tiles of the same number to create a new tile with their sum.
- **Random Tile Generation**: After each move, a new tile (2 or 4) is randomly placed on an empty spot.
- **Game Over**: The game ends when there are no possible moves left.
- **Win Condition**: The player wins by creating a tile with the number 2048.

## Getting Started

### Prerequisites

- Python 3.x
- Pygame library

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/2048-game.git
    cd 2048-game
    ```

2. Install Pygame:

    ```bash
    pip install pygame
    ```

3. Run the game:

    ```bash
    python game.py
    ```

## Gameplay

- Use the arrow keys to slide the tiles:
  - **Left Arrow**: Slide tiles left.
  - **Right Arrow**: Slide tiles right.
  - **Up Arrow**: Slide tiles up.
  - **Down Arrow**: Slide tiles down.

- Tiles with the same number merge into one when they touch:
  - For example, two tiles with the number 2 merge into one tile with the number 4.

- A new tile (2 or 4) is added to the grid after each move.

- The game ends when there are no possible moves left.

- The player wins by creating a tile with the number 2048.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by the original [2048 game](https://play2048.co/) by Gabriele Cirulli.
- Thanks to the Pygame community for their support and resources.

