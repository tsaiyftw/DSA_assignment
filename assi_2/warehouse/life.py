# Implements the LifeGrid ADT for use with the game of Life
# from newarray2d import Array2D
import tkinter as tk
from array import myArray2D


class GameGrid:
    # Defines constants to represent the cell states
    DEAD_CELL = 0
    LIVE_CELL = 1

    # Creates the game grid and initializes the cells to dead
    def __init__(self, numRows, numCols):
        # Allocate the 2D array for the grid
        self._grid = myArray2D(numRows, numCols)
        # Clear the grid
        self.configure(list())

    # Returns the number of rows in the grid
    def numRows(self):
        return self._grid.numRows()

    # Returns the number  of columns in the grid
    def numCols(self):
        return self._grid.numCols()

    # Configure the grid
    def configure(self, coordList):
        # Clear the game grid
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)

        # Set the indicated cells to be alive
        for coord in coordList:
            self.setCell(coord[0], coord[1])

    # Does the indicated cell contain a live organism
    def isLiveCell(self, row, col):
        return self._grid[row, col] == GameGrid.LIVE_CELL

    # Clear the indicated cell
    def clearCell(self, row, col):
        self._grid[row, col] = GameGrid.DEAD_CELL

    # Set the indicated cell to be alive
    def setCell(self, row, col):
        self._grid[row, col] = GameGrid.LIVE_CELL

    # Check where cell exists
    def isExistCell(self, row, col):

        try:
            if self._grid[row, col] == 1 or self._grid[row, col] == 0:
                return True
        except:
            return False

    # Returns the number of live neighbors
    def numLiveNeighbors(self, row, col):

        theNum = 0

        if row - 1 >= 0 and col - 1 >= 0:
            if self._grid[row - 1, col - 1] == 1:
                theNum += 1

        if row - 1 >= 0:
            if self._grid[row - 1, col] == 1:
                theNum += 1

        if row - 1 >= 0 and col + 1 < self._grid.numCols():
            if self._grid[row - 1, col + 1] == 1:
                theNum += 1

        if col - 1 >= 0 and col - 1 < self._grid.numCols():
            if self._grid[row, col - 1] == 1:
                theNum += 1

        if col + 1 < self._grid.numCols():
            if self._grid[row, col + 1] == 1:
                theNum += 1

        if col - 1 >= 0 and col - 1 < self._grid.numCols() and row + 1 < self.numRows():
            if self._grid[row + 1, col - 1] == 1:
                theNum += 1

        if row + 1 < self._grid.numRows():
            if self._grid[row + 1, col] == 1:
                theNum += 1

        if col + 1 < self._grid.numCols() and row + 1 < self.numRows():
            if self._grid[row + 1, col + 1] == 1:
                theNum += 1

        return theNum


# Generates the next generation of organisms
def evolve(grid):
    # List for storing the live cells of the next generation
    liveCells = list()

    # Iterate over the elements of the grid
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):

            # Determine the number of live neighbors for this cell
            neighbors = grid.numLiveNeighbors(i, j)

            # Add the (i,j) tuple to liveCells if this cell contains
            # a live organism in the next generation
            if neighbors == 2 and grid.isLiveCell(i, j) or (neighbors == 3):
                liveCells.append((i, j))

    # Reconfigure
    grid.configure(liveCells)


# Print the text-based representation
# use CAVAS GUI
DAALUCanvas1 = tk.Canvas(DAALUWIN)
DAALUCanvas1.delete("all")
width = 80
height = 80


def draw(grid):

    # for row in range(grid.numRows()):
    #     for col in range(grid.numCols()):
    #         if grid.isLiveCell(row, col):
    #             print("1 "),
    #         else:
    #             print("0 "),
    #     print("")
    # print("")

    for i in range(grid.numRows()):
        x1 = 80 + i * width
        x2 = x1 + width
        for j in range(grid.numCols()):
            y1 = 80 + j * height
            y2 = y1 + height
            DAALUCanvas1.create_rectangle(x1, y1, x2, y2, fill="lightgreen")
            xc = int((x1 + x2) / 2)
            yc = int((y1 + y2) / 2)

            if grid.isLiveCell(row, col):
                DAALUCanvas1.create_text(
                    xc, yc, fill="darkblue", font="Times 20 italic bold", text="1"
                )
            else:
                DAALUCanvas1.create_text(
                    xc, yc, fill="darkblue", font="Times 20 italic bold", text="0"
                )


# DAALUWIN = tk.Tk()
# DAALUWIN.title("Data Structure and Algorithm")
# DAALUWIN.geometry("1000x700+100+100")
# DAALUCanvas1 = tk.Canvas(DAALUWIN)
# DAALUCanvas1.delete("all")
# width = 80
# height = 80
# import random

# for i in range(3):
#     x1 = 80 + i * width
#     x2 = x1 + width
#     for j in range(3):
#         y1 = 80 + j * height
#         y2 = y1 + height
#         DAALUCanvas1.create_rectangle(x1, y1, x2, y2, fill="lightgreen")
#         xc = int((x1 + x2) / 2)
#         yc = int((y1 + y2) / 2)
#         ret = random.randint(1, 10)
#         if ret > 5:
#             DAALUCanvas1.create_text(
#                 xc, yc, fill="darkblue", font="Times 20 italic bold", text="O"
#             )
#         else:
#             DAALUCanvas1.create_text(
#                 xc, yc, fill="darkblue", font="Times 20 italic bold", text="X"
#             )


def gameOfLife():

    # Define the initial configuration of live cells
    INIT_CONFIG = [
        (1, 1),
        (1, 2),
        (1, 5),
        (1, 6),
        (2, 3),
        (2, 4),
        (3, 3),
        (3, 5),
        (3, 7),
        (3, 1),
        (4, 6),
        (5, 1),
        (5, 0),
        (5, 5),
        (5, 6),
        (6, 3),
        (6, 4),
        (6, 5),
        (6, 6),
    ]

    # Set the size of the grid
    GRID_WIDTH = 8
    GRID_HEIGHT = 8

    # Indicate the number of generation
    NUM_GENS = 5

    # Construct the game grid and configure it
    grid = GameGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)

    # Play the game
    draw(grid)
    for _ in range(NUM_GENS):
        evolve(grid)
        draw(grid)


if __name__ == "__main__":
    gameOfLife()
