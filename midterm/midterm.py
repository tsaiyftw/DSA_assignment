from myarray import myArray2D
from myarray import linearSet
from myarray import binarySet
from myarray import SparseMatrix

# read matrix A data from txt file
m_data = open("mA.txt", "r")

# set the default value of matrix A
ROW_AMOUNT = 5
COLUMN_AMOUNT = 18

# create new empty matrix
matrix_row_major = myArray2D(50, 50)
matrix_column_major = myArray2D(50, 50)

# load the values in text file to 2D array
def createMatrix():
    i = 0
    # read each line in the text file
    for entry in m_data:
        entry_row = entry.split()
        for j in range(len(entry_row)):
            matrix_row_major[i, j] = int(entry_row[j])
            # create the transpose of matrix A (flip the 2D array index number)
            matrix_column_major[j, i] = matrix_row_major[i, j]
        i += 1
    return matrix_row_major, matrix_column_major


createMatrix()

# find the value by index number in 1D array, passing the desired index as parameters
def findNumber(ind_row, ind_col):
    # matrix A with 5 rows and 18 columns
    # in the 2D array row-mojor matrix => offset number: 18
    i_num, j_num = ind_row // COLUMN_AMOUNT, ind_row % COLUMN_AMOUNT
    # in the 2D array column-mojor matrix => offset number: 5
    i_num_col, j_num_col = ind_col // ROW_AMOUNT, ind_col % ROW_AMOUNT
    print(f"Row-major the {ind_row}th number:", matrix_row_major[i_num, j_num])
    print(
        f"Column-major the {ind_col}th number:",
        matrix_column_major[i_num_col, j_num_col],
    )
    return matrix_row_major[i_num, j_num], matrix_column_major[i_num_col, j_num_col]


findNumber(70, 65)

# multiply matrix A and its transpose matrix
def multiplyM_TM():
    mul_A_T = myArray2D(5, 5)
    lst = []
    for i in range(ROW_AMOUNT):
        for j in range(ROW_AMOUNT):
            total = 0
            for k in range(COLUMN_AMOUNT):
                total += matrix_row_major[i, k] * matrix_column_major[k, j]
            mul_A_T[i, j] = total
            # store the results of the multiplication to a list
            lst.append(mul_A_T[i, j])
    # show the results in the form similar to a matrix (5*5)
    print("The multiplication results: ")
    for i in range(0, len(lst), ROW_AMOUNT):
        print(lst[i : i + ROW_AMOUNT])
    return mul_A_T


multiplyM_TM()

# create a new empty set
mA_set = linearSet()

# load data from text file to set
def transferMatrixToSet():
    # read data from txt and store in a list
    m_data = open("mA.txt", "r")
    data_line = m_data.read()
    entry_lst = data_line.replace("\n", " ").split()
    m_data.close()
    # add the value in the list to the set
    for i in range(len(entry_lst)):
        mA_set.add(int(entry_lst[i]))
    return print("The values in Set A: ", mA_set._theElements)


transferMatrixToSet()

m_biSet = binarySet()


def addTobinarySet():
    # read data from txt and store in a list
    m_data = open("mA.txt", "r")
    data_line = m_data.read()
    entry_lst = data_line.replace("\n", " ").split()
    m_data.close()
    # add the value in the list to the set
    for i in range(len(entry_lst)):
        # print("before", m_biSet._theElements)
        m_biSet.add(int(entry_lst[i]))
        # print("after: ", m_biSet._theElements)
    return print("The values in binary Set A: ", m_biSet._theElements)


addTobinarySet()

# create a new empty sparse matrix
sparseM = SparseMatrix(10, 10)

# load the non-zero element in matrix A to Sparse matrix ADT
def toSparseMatrix():
    for i in range(ROW_AMOUNT):
        for j in range(COLUMN_AMOUNT):
            sparseM[i, j] = matrix_row_major[i, j]
    for ndx in range(len(sparseM._elementList)):
        print(
            f"{ndx}th non-zero element in matrix A[ {sparseM._elementList[ndx].row},{sparseM._elementList[ndx].col}]: {sparseM._elementList[ndx].value}"
        )
    return sparseM


toSparseMatrix()

# sort a sequence in ascending order using the bubble sort algorithm


def bubbleSort(seq):
    n = len(seq)
    swap_count = 0
    # perform n-i bubble operations on the sequence
    for i in range(n - 1):
        # bubble the largest item to the right
        for j in range(n - 1 - i):
            if seq[j] > seq[j + 1]:  # swap the j and j+1 items
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                swap_count += 1
    print(swap_count)
    return seq


m_data = open("mA.txt", "r")
data_line = m_data.read()
entry_lst = data_line.replace("\n", " ").split()
m_data.close()
lst_com = [int(entry_lst[i]) for i in range(len(entry_lst))]
big_lst = [
    lst_com[j : j + COLUMN_AMOUNT] for j in range(0, len(lst_com), COLUMN_AMOUNT)
]
for i in range(len(big_lst)):
    bubbleSort(big_lst[i])
    print(bubbleSort(big_lst[i]))
