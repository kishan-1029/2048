#pip install pygame
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 4
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
GRID_MARGIN = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TILE_COLORS = {
    0: (204, 192, 179),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

# Initialize the game board
board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

def draw_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            value = board[row][col]
            pygame.draw.rect(
                screen,
                TILE_COLORS[value],
                [
                    col * GRID_WIDTH + GRID_MARGIN,
                    row * GRID_HEIGHT + GRID_MARGIN,
                    GRID_WIDTH - GRID_MARGIN * 2,
                    GRID_HEIGHT - GRID_MARGIN * 2,
                ],
            )
            if value != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(value), True, BLACK)
                text_rect = text.get_rect(center=(
                    col * GRID_WIDTH + GRID_WIDTH // 2,
                    row * GRID_HEIGHT + GRID_HEIGHT // 2,
                ))
                screen.blit(text, text_rect)

def add_random_tile():
    empty_cells = [(row, col) for row in range(GRID_SIZE) for col in range(GRID_SIZE) if board[row][col] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 2 if random.random() < 0.9 else 4

def slide_tiles(direction):
    if direction in ["left", "right"]:
        for row in range(GRID_SIZE):
            non_empty_tiles = [tile for tile in board[row] if tile != 0]
            empty_tiles = [0] * (GRID_SIZE - len(non_empty_tiles))
            board[row] = non_empty_tiles + empty_tiles if direction == "left" else empty_tiles + non_empty_tiles
    elif direction in ["up", "down"]:
        for col in range(GRID_SIZE):
            column = [board[row][col] for row in range(GRID_SIZE) if board[row][col] != 0]
            empty_tiles = [0] * (GRID_SIZE - len(column))
            column = column + empty_tiles if direction == "up" else empty_tiles + column
            for row in range(GRID_SIZE):
                board[row][col] = column[row]

def combine_tiles(direction):
    if direction == "left":
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE - 1):
                if board[row][col] == board[row][col + 1] and board[row][col] != 0:
                    board[row][col] *= 2
                    board[row][col + 1] = 0
    elif direction == "right":
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE - 1, 0, -1):
                if board[row][col] == board[row][col - 1] and board[row][col] != 0:
                    board[row][col] *= 2
                    board[row][col - 1] = 0
    elif direction == "up":
        for col in range(GRID_SIZE):
            for row in range(GRID_SIZE - 1):
                if board[row][col] == board[row + 1][col] and board[row][col] != 0:
                    board[row][col] *= 2
                    board[row + 1][col] = 0
    elif direction == "down":
        for col in range(GRID_SIZE):
            for row in range(GRID_SIZE - 1, 0, -1):
                if board[row][col] == board[row - 1][col] and board[row][col] != 0:
                    board[row][col] *= 2
                    board[row - 1][col] = 0

def move_tiles(direction):
    slide_tiles(direction)
    combine_tiles(direction)
    slide_tiles(direction)

def is_game_over():
    for row in board:
        if 0 in row:
            return False
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE - 1):
            if board[row][col] == board[row][col + 1]:
                return False
    for col in range(GRID_SIZE):
        for row in range(GRID_SIZE - 1):
            if board[row][col] == board[row + 1][col]:
                return False
    return True

def has_won():
    for row in board:
        if 2048 in row:
            return True
    return False

def main():
    add_random_tile()
    add_random_tile()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not is_game_over():
                    if event.key == pygame.K_LEFT:
                        move_tiles("left")
                    elif event.key == pygame.K_RIGHT:
                        move_tiles("right")
                    elif event.key == pygame.K_UP:
                        move_tiles("up")
                    elif event.key == pygame.K_DOWN:
                        move_tiles("down")
                    add_random_tile()
                if has_won():
                    print("You Win!")
                    running = False
                elif is_game_over():
                    print("Game Over")
                    running = False

        screen.fill(WHITE)
        draw_grid()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
