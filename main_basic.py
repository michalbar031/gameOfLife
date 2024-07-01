def print_grid(grid):
    for row in grid:
        print(' '.join(['█' if cell else ' ' for cell in row]))


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

def main():

    n=40
    grid = [[0 for _ in range(n)] for _ in range(n)]
    alive_init = [(4, 4), (4, 5), (5, 6), (6, 4), (6, 5), (6, 6), (6, 7), (7, 5), (7, 6),(25,24),(25,25),(25,26),(15,12),]
    init_grid(grid, alive_init)



    generations = 100  # Number of generations to simulate.

    for generation in range(generations):
        print(f"Generation {generation + 1}")
        print_grid(grid)
        grid = next_generation(grid)
        print("\n")


if __name__ == "__main__":
    main()


