# A simple game of life implementation in python

import pygame
from constants import CELL_ACTIVE, CELL_INACTIVE, GRID_WIDTH, GRID_HEIGHT
from game_of_life_patterns import get_gun_one_state, get_gun_two_state

# Constants
WIDTH = 800
HEIGHT = 800
FPS = 1
CELL_SIZE = 10
# Colors
# Set active and inactive cell colors
ACTIVE_CELL_COLOR = (0, 0, 0)
INACTIVE_CELL_COLOR = (255, 255, 255)
# Set background color
GRID_COLOR = (50, 50, 50)

# initialize the grids
GRID = [[CELL_INACTIVE for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)]

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()


def set_initial_state():
    """Let the player set the initial state by clicking on cells"""
    # empty the grid
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            GRID[x][y] = CELL_INACTIVE

    running = True
    while running:
        # Keep loop running at the right speed
        clock.tick(60)

        # Process input (events)
        for event in pygame.event.get():
            # Check for closing the window
            if event.type == pygame.QUIT:
                running = False

        # Update
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            pos = pygame.mouse.get_pos()
            GRID[pos[0] // CELL_SIZE][pos[1] // CELL_SIZE] = CELL_ACTIVE
        # if left mouse button is pressed close the current loop
        if mouse[2]:
            running = False

        # if key '1' is pressed set the initial state to the gun one state
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_1]:
            new_grid = get_gun_one_state()
            # copy the new grid to the current grid
            copy_grid(new_grid, GRID)

            running = False
        # if key '2' is pressed set the initial state to the gun two state
        if pressed[pygame.K_2]:
            new_grid = get_gun_two_state()
            copy_grid(new_grid, GRID)
            running = False

        # Draw / render
        screen.fill(GRID_COLOR)
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if GRID[x][y] == CELL_ACTIVE:
                    pygame.draw.rect(
                        screen,
                        ACTIVE_CELL_COLOR,
                        (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                    )
                else:
                    pygame.draw.rect(
                        screen,
                        INACTIVE_CELL_COLOR,
                        (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                    )
        pygame.display.flip()


def copy_grid(grid_to_copy, grid_to_copy_to):
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            grid_to_copy_to[x][y] = grid_to_copy[x][y]


def run_game_loop():
    """Run the game loop"""
    running = True
    while running:
        # Keep loop running at the right speed
        clock.tick(FPS)

        # Process input (events)
        for event in pygame.event.get():
            # Check for closing the window
            if event.type == pygame.QUIT:
                running = False

        # Copy the next generation grid to the current grid
        copy_grid(get_next_gen_grid(), GRID)

        # Draw / render
        render_grid()

        # if key 'r' is pressed start a new game
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_r]:
            print("Starting a new game")
            start_game()
        # if q is pressed quit the game
        if pressed[pygame.K_q]:
            print("Quitting the game")
            running = False

        pygame.display.flip()

    pygame.quit()


def get_next_gen_grid():
    next_gen_grid = [
        [CELL_INACTIVE for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)
    ]

    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            next_gen_grid[x][y] = get_next_state(x, y)

    return next_gen_grid


def render_grid():
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if GRID[x][y] == CELL_ACTIVE:
                pygame.draw.rect(
                    screen,
                    ACTIVE_CELL_COLOR,
                    (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                )
            else:
                pygame.draw.rect(
                    screen,
                    INACTIVE_CELL_COLOR,
                    (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                )


def get_next_state(x, y):
    """Get the next state of the cell at x, y. The rule are as follows:
    1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """
    # Get the number of active neighbors
    active_neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x + i >= 0 and x + i < GRID_WIDTH and y + j >= 0 and y + j < GRID_HEIGHT:
                if i == 0 and j == 0:
                    continue
                if GRID[x + i][y + j] == CELL_ACTIVE:
                    active_neighbors += 1

    # Apply the rules
    # 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    if GRID[x][y] == CELL_ACTIVE and active_neighbors < 2:
        return CELL_INACTIVE
    # 2. Any live cell with two or three live neighbours lives on to the next generation.
    if GRID[x][y] == CELL_ACTIVE and (active_neighbors == 2 or active_neighbors == 3):
        return CELL_ACTIVE
    # 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    if GRID[x][y] == CELL_ACTIVE and active_neighbors > 3:
        return CELL_INACTIVE
    # 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    if GRID[x][y] == CELL_INACTIVE and active_neighbors == 3:
        return CELL_ACTIVE


def start_game():
    set_initial_state()
    run_game_loop()


if __name__ == "__main__":
    start_game()
