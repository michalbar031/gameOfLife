import pygame
import sys


def draw_grid(screen, grid, cell_size):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            color = (255, 255, 255) if cell else (50, 50, 50)  # White for alive, gray for dead
            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, (100, 100, 100), (j * cell_size, i * cell_size, cell_size, cell_size), 1)  # Grid lines


def get_neighbors(grid, x, y):
    neighbors = [
        (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
        (x, y - 1), (x, y + 1),
        (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
    ]
    return [(i, j) for i, j in neighbors if 0 <= i < len(grid) and 0 <= j < len(grid[0])]


def count_alive_neighbors(grid, x, y):
    neighbors = get_neighbors(grid, x, y)
    return sum([grid[i][j] for i, j in neighbors])


def next_generation(grid):
    new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            alive_neighbors = count_alive_neighbors(grid, i, j)
            if grid[i][j] == 1:  # The cell is alive.
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_grid[i][j] = 0  # Cell dies.
                else:
                    new_grid[i][j] = 1  # Cell stays alive.
            else:  # The cell is dead.
                if alive_neighbors == 3:
                    new_grid[i][j] = 1  # Cell becomes alive.
                else:
                    new_grid[i][j] = 0  # Cell stays dead.
    return new_grid


def init_grid(grid, alive_init):
    for i, j in alive_init:
        grid[i][j] = 1
    return grid


#  initial patterns
def add_block(grid, x, y):
    block = [(x, y), (x, y + 1), (x + 1, y), (x + 1, y + 1)]
    return block


def add_blinker(grid, x, y):
    blinker = [(x, y), (x, y + 1), (x, y + 2)]
    return blinker


def add_glider(grid, x, y):
    glider = [(x, y + 1), (x + 1, y + 2), (x + 2, y), (x + 2, y + 1), (x + 2, y + 2)]
    return glider


def draw_text(screen, text, pos, font_size=20, color=(255, 255, 255)):
    font = pygame.font.Font(pygame.font.get_default_font(), font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)


def draw_button(screen, text, pos, width, height, color, font_size=20):
    rect = pygame.Rect(pos[0], pos[1], width, height)
    pygame.draw.rect(screen, color, rect)
    draw_text(screen, text, (pos[0] + 10, pos[1] + 5), font_size, (0, 0, 0))
    return rect


def main():
    n = 40  # the grid size

    pygame.init()

    cell_size = 15
    width, height = n * cell_size, n * cell_size + 140 # space for button and instructions
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Game of Life')

    # initialize grid
    grid = [[0 for _ in range(n)] for _ in range(n)]

    # add some initial patterns
    alive_init = add_block(grid, 10, 10)
    alive_init += add_blinker(grid, 20, 20)
    alive_init += add_glider(grid, 16, 23)
    alive_init += add_glider(grid, 30, 30)
    init_grid(grid, alive_init)

    running = True
    simulate = False
    clock = pygame.time.Clock()

    while running:
        screen.fill((0, 0, 0))  # clear screen with black
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if y < height - 60:
                    grid_x = x // cell_size
                    grid_y = y // cell_size
                    grid[grid_y][grid_x] = 1 if grid[grid_y][grid_x] == 0 else 0
                elif start_button.collidepoint(event.pos):
                    simulate = not simulate

        if simulate:
            grid = next_generation(grid)
            clock.tick(10)  # control the speed of simulation

        # draw current generation
        draw_grid(screen, grid, cell_size)

        #instructions
        draw_text(screen, "Click on cells to toggle them and make them alive or dead.", (10, height - 80), font_size=20, color=(255, 255, 255))
        draw_text(screen, "Press 'Start' to start/stop simulation.", (10, height - 60), font_size=20, color=(255, 255, 255))
        #button
        start_button = draw_button(screen, "Start" if not simulate else "Stop", (width // 2 - 50, height - 30), 100, 30, (200, 200, 200))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
