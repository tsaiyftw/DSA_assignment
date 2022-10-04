from __future__ import print_function
from life import GameGrid

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

GRID_WIDTH = 8
GRID_HEIGHT = 8

NUM_GENS = 2


def main():
    grid = GameGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)
    # play the game
    draw(grid)
    for i in range(NUM_GENS):
        evolve(grid)
        draw(grid)


def evolve(grid):
    # livecells of the next generation
    liveCells = list()
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            neighbors = grid.numLiveNeighbors(i, j)

            if (
                (neighbors == 2 and grid.isLiveCell(i, j))
                or (neighbors == 3 and grid.isLiveCell(i, j))
                or (not grid.isLiveCell(i, j) and neighbors == 3)
            ):
                liveCells.append((i, j))  # appends the tuple
    grid.configure(liveCells)  # configures the grid using liveCells coord list


def draw(grid):
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            if grid.isLiveCell(i, j):
                print("x", sep=" ", end=" ")
            else:
                print("o", sep=" ", end=" ")
        print("\n")
    print("----next gen-----")


main()
