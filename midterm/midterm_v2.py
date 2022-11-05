from myarray import myArray2D, linearSet, binarySet, SparseMatrix


# method #2 to read entry element from txt file and store those elements in list of list
def readfile(input_file):
    big_lst = []
    with open(input_file) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            entry_row = lines[i].split()
            big_lst.append([int(entry) for entry in entry_row])
    return big_lst


data = readfile("mA.txt")

# load data to matrix
def loadMatrix(data):
    numRow = len(data)
    numCol = len(data[0])
    newMatrix = myArray2D(numRow, numCol)
    i = 0
    for row in data:
        for j in range(len(row)):
            newMatrix[i, j] = row[j]
        i += 1
    return newMatrix


# create a traspose matrix from origin matrix and store in 2D array ADT
def transpose(data):
    numRow = len(data)
    numCol = len(data[0])
    transposeM = myArray2D(numCol, numRow)
    for i in range(numRow):
        for j in range(numCol):
            transposeM[j, i] = data[i][j]
    return transposeM


# Given an index number and return its value in a 2D row-major array
def findValueRowMajor(data, index):
    matrixA = loadMatrix(data)
    i = index // len(data[0])
    j = index % len(data[0])
    return matrixA[i, j]


# Given an index number and return its value in a 2D row-column array
def findValueColMajor(data, index):
    matrixT = transpose(data)
    i = index // len(data)
    j = index % len(data)
    return matrixT[i, j]


def multiply(matrixA, matrixB):
    aRow = matrixA.numRows()
    aCol = matrixA.numCols()
    bRow = matrixB.numRows()
    bCol = matrixB.numCols()
    assert aCol == bRow
    res = myArray2D(aRow, bCol)
    for i in range(aRow):
        for j in range(bCol):
            total = 0
            for k in range(aCol):
                total += matrixA[i, k] * matrixB[k, j]
            res[i, j] = total
    return res


def printMatrix(matrix):
    numRow = matrix.numRows()
    numCol = matrix.numCols()
    lst = [matrix[i, j] for i in range(numRow) for j in range(numCol)]
    for i in range(0, len(lst), numCol):
        print(lst[i : i + numCol])


def toSet(matrix):
    numRow = matrix.numRows()
    numCol = matrix.numCols()
    entry_lst = [matrix[i, j] for i in range(numRow) for j in range(numCol)]
    newSet = binarySet()
    for i in range(len(entry_lst)):
        newSet.add(entry_lst[i])
    return newSet._theElements


def toLinearSet(matrix):
    numRow = matrix.numRows()
    numCol = matrix.numCols()
    entry_lst = [matrix[i, j] for i in range(numRow) for j in range(numCol)]
    newSet = linearSet()
    for i in range(len(entry_lst)):
        newSet.add(entry_lst[i])
    return newSet._theElements


def toSparseMatrix(matrix):
    numRow = matrix.numRows()
    numCol = matrix.numCols()
    newSparseMatrix = SparseMatrix(numRow, numCol)
    for i in range(numRow):
        for j in range(numCol):
            newSparseMatrix[i, j] = matrix[i, j]
    return newSparseMatrix


def printSparseMatrix(sparseMx):
    for i in range(len(sparseMx._elementList)):
        print(
            sparseMx._elementList[i].row,
            sparseMx._elementList[i].col,
            sparseMx._elementList[i].value,
        )


def bubbleSort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def swapCountBubble(lst):
    swap_count = 0
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap_count += 1
    return swap_count


# Q1:
print(findValueRowMajor(data, 70))
print(findValueColMajor(data, 65))

# Q2:
matrixA = loadMatrix(data)
matrixB = transpose(data)
matrix = multiply(matrixA, matrixB)
printMatrix(matrix)

# Q3:
print(toSet(matrixA))
print(toLinearSet(matrixA))

# Q4:
matrixSparse = toSparseMatrix(matrixA)
printSparseMatrix(matrixSparse)

# Q5:
for i in range(len(data)):
    print(f"The {i}th row swap count: {swapCountBubble(data[i])}")
    print(f"The {i}th row after sorted: {bubbleSort(data[i])}")
