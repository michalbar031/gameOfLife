# Conway's Game of Life
![image](https://github.com/michalbar031/gameOfLife/assets/81368958/d1b0df46-c024-4f95-a312-d37578317c0e)


This repository contains implementations of Conway's Game of Life, a cellular automaton devised by mathematician John Conway. The project includes a basic console implementation and a graphical user interface version using Pygame.

## Files

1. **environment.yml**: Environment configuration file for setting up the required dependencies using Conda.
2. **main_basic.py**: Basic console implementation of the Game of Life.
3. **UI_pygame.py**: Pygame implementation of the Game of Life with Pygame.

## Setup

To set up the environment and run the project, follow these steps:

### 1. Clone the Repository
Clone the repository using:
```sh
git clone https://github.com/michalbar031/gameOfLife.git
```
Change directory to:
```sh
cd gameOfLife
```
### 2. Create the Conda Environment
```sh
conda env create -f environment.yml
```
then activate it:
```sh
conda activate gameOfLife
```

### 3. Run the Pygame Implementation
In this implementation:
1. The grid size is 40x40.
2. The cell size is 15 pixels.
3. You can click on cells to toggle them alive or dead even during the simulation.
4. Press the "Start" button to start or stop the simulation.

You can run this implementation using:
```sh
python UI_pygame.py
```

### 4. Run the Basic Implementation
In this implementation:
1. The grid size is 40x40.
2. The simulation runs for 100 generations.
3. Initial alive cells are specified in the alive_init list.
   
You can run the basic implementation using:
```sh
python main_basic.py
```

### Explanation of Files
environment.yml
The environment.yml file specifies the dependencies needed for the project. It is used to create a Conda environment with all the required packages.

main_basic.py
This is the basic console implementation of Conway's Game of Life. It includes the following functions:

print_grid(grid): Prints the current state of the grid to the console.
get_neighbors(grid, x, y): Returns the coordinates of neighboring cells.
count_alive_neighbors(grid, x, y): Counts the number of alive neighbors for a given cell.
next_generation(grid): Computes the next generation of the grid based on the rules of the game.
init_grid(grid, alive_init): Initializes the grid with the initial alive cells.
You can modify the alive_init list to change the initial configuration of alive cells.

UI_pygame.py
This is the Pygame GUI implementation of Conway's Game of Life. It includes additional functions for handling the graphical interface:

draw_grid(screen, grid, cell_size): Draws the grid on the Pygame screen.
draw_text(screen, text, pos, font_size, color): Draws text on the screen.
draw_button(screen, text, pos, width, height, color, font_size): Draws a button on the screen.
