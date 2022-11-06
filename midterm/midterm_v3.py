from myarray import myArray2D, linearSet, binarySet, SparseMatrix


# read entry element from txt file and store those elements in a list of list
def readfile(input_file_pathway):
    big_lst = []
    with open(input_file_pathway) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            entry_row = lines[i].split()
            big_lst.append([int(entry) for entry in entry_row])
    return big_lst


# load the file data in the list of list to a 2D matrix (i.e. row-major)
def loadMatrix(data):
    numRow = len(data)
    numCol = len(data[0])
    newMatrix = myArray2D(numRow, numCol)
    for i in range(numRow):
        for j in range(numCol):
            newMatrix[i, j] = data[i][j]
    return newMatrix


# create a traspose matrix of an origin matrix and store in 2D array ADT (i.e. column-major)
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


# Given an index number and return its value in a 2D column-major array
def findValueColMajor(data, index):
    matrixT = transpose(data)
    i = index // len(data)
    j = index % len(data)
    return matrixT[i, j]


# multiply two matrix and return the result as a 2D matrix
def multiply(matrixA, matrixB):
    aRow, aCol = matrixA.numRows(), matrixA.numCols()
    bRow, bCol = matrixB.numRows(), matrixB.numCols()
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
    numRow, numCol = matrix.numRows(), matrix.numCols()
    lst = [matrix[i, j] for i in range(numRow) for j in range(numCol)]
    for i in range(0, len(lst), numCol):
        print(lst[i : i + numCol])


# load each entry in a matrix to a list
def matrixToList(matrix):
    numRow, numCol = matrix.numRows(), matrix.numCols()
    entry_lst = [matrix[i, j] for i in range(numRow) for j in range(numCol)]
    return entry_lst


# add the values in a list to a set with a binary search implement
def toSet(lst):
    newSet = binarySet()
    for entry in lst:
        newSet.add(entry)
    return newSet._theElements


# add the values in a list to a set with a linear search implement
def toLinearSet(lst):
    newSet = linearSet()
    for entry in lst:
        newSet.add(entry)
    return newSet._theElements


# transform 2D array to a sparse matrix with implement of 2D array (removing zero entry)
def toSparseMatrix(matrix):
    numRow, numCol = matrix.numRows(), matrix.numCols()
    newSparseMatrix = SparseMatrix(numRow, numCol)
    for i in range(numRow):
        for j in range(numCol):
            newSparseMatrix[i, j] = matrix[i, j]
    return newSparseMatrix


# retrieve the value in the sparse metrix and return a list showing the row, column, value
def printSparseMatrix(sparseMx):
    sparseMatrixLst = []
    for entry in sparseMx._elementList:
        sparseMatrixLst.append([entry.row, entry.col, entry.value])
    print(sparseMatrixLst)


#  sort a list by bubble sorting and return the swap count for sorting the list
def swapCountBubble(lst):
    swap_count = 0
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap_count += 1
    return swap_count


# Q1:
data = readfile("mA.txt")
print("Row-major index 70:", findValueRowMajor(data, 70))
print("Column-major index 65: ", findValueColMajor(data, 65))

# Q2:
matrixA = loadMatrix(data)
matrixB = transpose(data)
matrix = multiply(matrixA, matrixB)
print("Multiply matrix A and its transpose matrix:")
printMatrix(matrix)

# Q3:
lst = matrixToList(matrixA)
print("Store the values in matrix to a set with binary search implement: ", toSet(lst))
print(
    "Stor the values in matrix to a set with linear search implement:: ",
    toLinearSet(lst),
)

# Q4:
matrixSparse = toSparseMatrix(matrixA)
print(
    "Store the non-zeore values in a sparse matrix to a list(Format: [row index, column indx, value]): "
)
printSparseMatrix(matrixSparse)

# Q5:
for i in range(len(data)):
    count = swapCountBubble(data[i])
    print(f"The {i}th row swap count: {count}")
    print(f"The {i}th row after sorted: {data[i]}")
