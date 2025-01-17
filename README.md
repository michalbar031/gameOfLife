
# **Conway's Game of Life**
<img align="right" width="350" height="250" src="https://github.com/michalbar031/gameOfLife/assets/81368958/d1b0df46-c024-4f95-a312-d37578317c0e">


This repository contains implementations of Conway's Game of Life, a cellular automaton devised by mathematician John Conway.
The project includes a basic console implementation and a graphical user interface version using Pygame.

**Files:**

1. **```environment.yml```**: Environment configuration file for setting up the required dependencies using Conda.
2. **```main_basic.py```**: Basic console implementation of the Game of Life.
3. **```UI_pygame.py```**: Pygame implementation of the Game of Life with Pygame.

# **Setup**

To set up the environment and run the project, follow these steps:

## 1. Clone the Repository
Clone the repository using:
```sh
git clone https://github.com/michalbar031/gameOfLife.git
```
Change directory to:
```sh
cd gameOfLife
```
## 2. Create the Conda Environment
```sh
conda env create -f environment.yml
```
then activate it:
```sh
conda activate gameOfLife
```

## 3. Run the Pygame Implementation
<img align="right" width="340" height="470" src="https://github.com/michalbar031/gameOfLife/assets/81368958/51036b4e-f95f-4b2c-bcb6-861b1ec59101">

In this implementation:

1. The grid size is 40x40.
   to change it you can modify n:
   ```python
   n = 40  # the grid size
   ```
2. The cell size is 15 pixels.
3. ```alive_init``` is a list of tuples where each tuple represents the coordinates of a cell that should be alive at the start of the simulation.
   This list is used to initialize the grid with a specific configuration of alive cells. When running the simulation the user can update them. 
4. You can click on cells to toggle them alive or dead even during the simulation.
5. Press the "Start" button to start or stop the simulation.

You can run this implementation using:
```sh
python UI_pygame.py
```

## 4. Run the Basic Implementation
In this implementation:

1. The grid size is 40x40.
2. The simulation runs for 100 generations.
3. Initial alive cells are specified in the alive_init list.
   
You can run the basic implementation using:
```sh
python main_basic.py
```
