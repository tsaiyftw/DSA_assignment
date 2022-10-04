#####################################################################################
def PAGES(n):
    sss = []
    ttt = []  ### initial to be null
    iii = -1

    iii = iii + 1
    if int(n) == iii:  ### page 0
        sss = """Game of Life """  ### sss is a string

    iii = iii + 1
    if int(n) == iii:
        sss = """import ctypes
class myArray:
    # Creates an array with size elements.
    def __init__( self, size ):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element
        self.clear( None )


    # Returns the size of the array
    def __len__( self ):
        return self._size
    # Gets the contents of the index element
    def __getitem__( self, index ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[ index ]

    # Puts the value in the array element at index position
    def __setitem__( self, index, value):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[ index ] = value

    # Clears the array by setting each element to the given value
    def clear( self, value ):
        for i in range( len(self) ):
            self._elements[i] = value

    # Returns the array's iterator for traversing the elements
    def __iter__( self ):
        return _ArrayIterator( self._elements )



# An iterator for the Array ADT.
class _ArrayIterator:
    def __init__( self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__( self ):
        return self

    def __next__( self ):
        if self._curNdx < len( self._arrayRef ):
            entry = self._arrayRef[ self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration

"""

    iii = iii + 1
    if int(n) == iii:
        sss = """# Implementation of the Array2D ADT using an array of arrays
class myArray2D:
    #Creates a 2-D array of size numRows * numCols.
    def __init__( self, numRows, numCols ):
        # Create a 1-D array to store an array reference for each row
        self._theRows = myArray( numRows )

        # Create the 1-D array to store each row of the 2-D array
        for i in range( numRows ):
            self._theRows[i] = myArray( numCols )

    # Returns the number of rows in the 2-D array
    def numRows( self ):
        return len(self._theRows)

    # Returns the number of columns in the 2-D array
    def numCols( self ):
        return len(self._theRows[0])

    # Clears the array by setting every element to the given value
    def clear( self, value ):
        for row in range( self.numRows() ):
            self._theRows[row].clear( value )

    # Gets the contents of the element at position [i, j]
    def __getitem__( self, ndxTuple ):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
            "Array subscripts out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]

    # Sets the contents of the element at position [i, j] to value.
    def __setitem__( self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
            "Array subscripts out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value
"""
    iii = iii + 1
    if int(n) == iii:
        sss = """2.5 Application: The Game of Life
英國數學家約翰·康威（John H. Conway）設計的生命遊戲是一種單人紙牌遊戲，類似於“生物社會的興衰和交替”。該遊戲實際上是一個零玩家遊戲，由 Martin Gardner 在 1970 年 10 月號的《科學美國人》雜誌的數學遊戲專欄中首次介紹。自推出以來，Life 引起了廣泛的關注並得到了廣泛的研究，因為它可以用來觀察複雜的系統或模式如何從一組簡單的規則演變而來。生命遊戲是現代數學領域中稱為元胞自動機的一個問題的早期例子。

The game of Life, devised by British mathematician John H. Conway, is a Solitaire- type game that is analogous with “the rise, fall and alternations of a society of living organisms.” The game, which is actually a zero-player game, was first introduced by Martin Gardner in his Mathematical Games column in the October 1970 issue of Scientific American. Since its introduction, Life has attracted much attention and has been widely studied as it can be used to observe how complex systems or patterns can evolve from a simple set of rules. The game of Life was an early example of a problem in the modern field of mathematics called cellular automata."""

    iii = iii + 1
    if int(n) == iii:
        sss = """2.5.1 The Rules of the Game:
遊戲使用無限大小的矩形網格單元格，其中每個單元格要么是空的，要么被有機體佔據。被佔用的細胞據說是活的，而空的細胞是死的。遊戲在特定的時間段內進行，每回合根據當前配置中活生物體的排列創建一個新的“世代”。通過對當前配置中的每個單元應用以下四個基本規則來確定下一代單元的狀態：

The game uses an infinite-sized rectangular grid of cells in which each cell is either empty or occupied by an organism. The occupied cells are said to be alive, whereas the empty ones are dead. The game is played over a specific period of time with each turn creating a new “generation” based on the arrangement of live organisms in the current configuration. The status of a cell in the next generation is determined by applying the following four basic rules to each cell in the current configuration:"""

    iii = iii + 1
    if int(n) == iii:
        sss = """2.5.1 The Rules of the Game:
1. 如果一個細胞是活著的並且有兩個或三個活著的鄰居，那麼該細胞在下一代仍然活著。鄰居是緊鄰一個單元格的八個單元格：垂直、水平和對角線。
2. 一個沒有活鄰居或一個活鄰居的活細胞在下一代因孤立而死。
3. 具有四個或更多活鄰居的活細胞在下一代死於人口過剩。
4. 一個死細胞，恰好有三個活的鄰居，會導致出生，並在下一代中活過來。所有其他死亡細胞在下一代仍然死亡。 

1. If a cell is alive and has either two or three live neighbors, the cell remains alive in the next generation. The neighbors are the eight cells immediately surrounding a cell: vertically, horizontally, and diagonally.
2. A living cell that has no live neighbors or a single live neighbor dies from isolation in the next generation.
3. A living cell that has four or more live neighbors dies from overpopulation in the next generation.
4. A dead cell with exactly three live neighbors results in a birth and becomes alive in the next generation. All other dead cells remain dead in the next generation. 
"""

    iii = iii + 1
    if int(n) == iii:
        sss = """# Implementation of the Array2D ADT using an array of arrays
class myArray2D:
    #Creates a 2-D array of size numRows * numCols.
    def __init__( self, numRows, numCols ):
        # Create a 1-D array to store an array reference for each row
        self._theRows = myArray( numRows )

        # Create the 1-D array to store each row of the 2-D array
        for i in range( numRows ):
            self._theRows[i] = myArray( numCols )

    # Returns the number of rows in the 2-D array
    def numRows( self ):
        return len(self._theRows)

    # Returns the number of columns in the 2-D array
    def numCols( self ):
        return len(self._theRows[0])

    # Clears the array by setting every element to the given value
    def clear( self, value ):
        for row in range( self.numRows() ):
            self._theRows[row].clear( value )

    # Gets the contents of the element at position [i, j]
    def __getitem__( self, ndxTuple ):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
            "Array subscripts out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]

    # Sets the contents of the element at position [i, j] to value.
    def __setitem__( self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
            "Array subscripts out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value
"""

    iii = iii + 1
    if int(n) == iii:
        sss = r"""#life.py: 
# Implements the LifeGrid ADT for use with the game of Life
#from newarray2d import Array2D
#from array import myArray2D

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

        if row -1 >= 0 and col - 1 >= 0:
            if self._grid[row-1,col-1] == 1:
                theNum += 1

        if row - 1 >= 0:
            if self._grid[row-1,col] == 1:
                theNum += 1

        if row -1 >= 0 and col + 1 < self._grid.numCols():
            if self._grid[row-1,col+1] == 1:
                theNum += 1

        if col -1 >= 0 and col - 1 < self._grid.numCols():
            if self._grid[row,col-1] == 1:
                theNum += 1

        if col + 1 < self._grid.numCols():
            if self._grid[row,col+1] == 1:
                theNum += 1

        if col -1 >= 0 and col - 1 < self._grid.numCols() and row+1 < self.numRows():
            if self._grid[row+1,col-1] == 1:
                theNum += 1

        if row +1 < self._grid.numRows():    
            if self._grid[row+1,col] == 1:
                theNum += 1

        if col + 1 < self._grid.numCols() and row+1 < self.numRows():
            if self._grid[row+1,col+1] == 1:
                theNum += 1

        return theNum
"""

    iii = iii + 1
    if int(n) == iii:
        sss = r"""
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
            if (neighbors == 2 and grid.isLiveCell(i,j) or (neighbors == 3)):
                liveCells.append((i,j))

    # Reconfigure
    grid.configure(liveCells)
"""
    iii = iii + 1
    if int(n) == iii:
        sss = r"""
# Print the text-based representation

def draw(grid):
    DAALUCanvas1.delete('all') 
    width=50
    height=50
    for col in range(grid.numRows()):
        x1=50+col*width
        x2=x1+width
        for row in range(grid.numCols()):
            y1=50+row*height
            y2=y1+height
            DAALUCanvas1.create_rectangle(x1,y1,x2,y2,fill='lightgreen')
            xc=int((x1+x2)/2)
            yc=int((y1+y2)/2)               
            if grid.isLiveCell(row, col):
                DAALUCanvas1.create_text(xc,yc,fill="red",font="Times 20 italic bold",text="1")
                print("1", row, col,xc,yc)
            else:
                DAALUCanvas1.create_text(xc,yc,fill="black",font="Times 20 italic bold",text="0")
                print("0",row, col,xc,yc)

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
        (6, 6)
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

"""

    iii = iii + 1
    if int(n) == iii:
        sss = r"""DAALUCanvas1.delete('all') 
width=80
height=80
import random
for i in range(3):
    x1=80+i*width
    x2=x1+width
    for j in range(3):
        y1=80+j*height
        y2=y1+height
        DAALUCanvas1.create_rectangle(x1,y1,x2,y2,fill='lightgreen')
        xc=int((x1+x2)/2)
        yc=int((y1+y2)/2)
        ret=random.randint(1,10)
        if ret>5:
           DAALUCanvas1.create_text(xc,yc,fill="darkblue",font="Times 20 italic bold",text="O")
        else:
           DAALUCanvas1.create_text(xc,yc,fill="darkblue",font="Times 20 italic bold",text="X")
"""
    return sss, ttt  ### output the result
