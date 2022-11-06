# Implements the Array ADT using array capabilities of the Ctypes module
import ctypes


class myArray:
    # Creates an array with size elements.
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element
        self.clear(None)

    # Returns the size of the array
    def __len__(self):
        return self._size

    # Gets the contents of the index element
    def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[index]

    # Puts the value in the array element at index position
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[index] = value

    # Clears the array by setting each element to the given value
    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    # Returns the array's iterator for traversing the elements
    def __iter__(self):
        return _ArrayIterator(self._elements)


# An iterator for the Array ADT.
class _ArrayIterator:
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration


# Implementation of the Array2D ADT using an array of arrays
class myArray2D:
    # Creates a 2-D array of size numRows * numCols.
    def __init__(self, numRows, numCols):
        # Create a 1-D array to store an array reference for each row
        self._theRows = myArray(numRows)

        # Create the 1-D array to store each row of the 2-D array
        for i in range(numRows):
            self._theRows[i] = myArray(numCols)

    # Returns the number of rows in the 2-D array
    def numRows(self):
        return len(self._theRows)

    # Returns the number of columns in the 2-D array
    def numCols(self):
        return len(self._theRows[0])

    # get the entries in the nth row
    def getRow(self, row):
        return self._theRows[row]

    # Clears the array by setting every element to the given value
    def clear(self, value):
        for row in range(self.numRows()):
            self._theRows[row].clear(value)

    # Gets the contents of the element at position [i, j]
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert (
            row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols()
        ), "Array subscripts out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]

    # Sets the contents of the element at position [i, j] to value.
    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert (
            row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols()
        ), "Array subscripts out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value


class binarySet:
    # Creates an empty set instance.
    def __init__(self):
        self._theElements = list()

    # Returns the number of items in the set.
    def __len__(self):
        return len(self._theElements)

    # Determines if an element is in the set.
    def __contains__(self, element):
        ndx = self._findPosition(element)
        return ndx < len(self._theElements) and self._theElements[ndx] == element

    # Adds a new unique element to the set.
    def add(self, element):
        if element not in self:
            ndx = self._findPosition(element)
            self._theElements.insert(ndx, element)

    # Removes an element from the set.
    def remove(self, element):
        assert element in self, "The element must be in the set."
        ndx = self._findPosition(element)
        self._theElements.pop(ndx)

    # Determines if this set is a subset
    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
            return True

    # Returns an iterator for traversing of setB.the list of items.
    def __iter__(self):
        return _SetIterator(self._theElements)

    # Finds the position of the element within the ordered list.
    def _findPosition(self, element):
        low = 0
        high = len(self._theElements) - 1
        while low <= high:
            mid = (high + low) // 2
            if self._theElements[mid] == element:
                return mid
            elif element < self._theElements[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low


class linearSet:
    # Creates an empty set instance.
    def __init__(self):
        self._theElements = list()

    # Returns the number of items in the set.
    def __len__(self):
        return len(self._theElements)

    # Determines if an element is in the set.
    def __contains__(self, element):
        return element in self._theElements

    # Adds a new unique element to the set.
    def add(self, element):
        if element not in self:
            self._theElements.append(element)

    # Removes an element from the set.
    def remove(self, element):
        assert element in self, "The element must be in the set."
        self._theElements.remove(element)

    # Determines if two sets are equal.
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)

    # Determines if this set is a subset of setB.
    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
            return True

    # Creates a new set from the union of this set and setB.
    def union(self, setB):
        newSet = linearSet()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

    # Returns an iterator for traversing the list of items.
    def __iter__(self):
        return _SetIterator(self._theElements)


class _SetIterator:
    def __init__(self, theList):
        self._bagItems = theList
        self._curItem = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curItem < len(self._bagItems):
            item = self._bagItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration


class SparseMatrix:
    #  create a sparse matrix of size numRows * numCols initialized to 0
    def __init__(self, numRows, numCols):
        self._numRows = numRows
        self._numCols = numCols
        self._elementList = list()

    # return the number of rows in the matrix
    def numRows(self):
        return self._numRows

    # return the number of columns in the matrix
    def numCols(self):
        return self._numCols

    # return the value of element(i,j): x[i,j]
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert (
            row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols()
        ), "Array subscripts out of range."
        ndx = self._findPosition(row, col)
        if ndx is not None:
            val = self._elementList[ndx].value
            return val
        else:
            return None

    # set the value of element(i,j) to value s: x[i,j] = s
    def __setitem__(self, ndxTuple, scalar):
        ndx = self._findPosition(ndxTuple[0], ndxTuple[1])
        if ndx is not None:  # if the element is found in the list
            if scalar != 0.0:
                self._elementList[ndx].value = scalar
            else:
                self._elementList.pop(ndx)
        else:  # if the element is not zero and not in the list
            if scalar != 0.0:
                element = _MatrixElement(ndxTuple[0], ndxTuple[1], scalar)
                self._elementList.append(element)

    # scale the matrix by the given scalar
    def scaleBy(self, scalar):
        for element in self._elementList:
            element.value *= scalar

    # helper method used to find a specific matrix element(row,col) in the list of non-zero entries.
    # None is returned if the element is not found
    def _findPosition(self, row, col):
        n = len(self._elementList)
        for i in range(n):
            if row == self._elementList[i].row and col == self._elementList[i].col:
                return i  # return the index of the element if found
        return None  # return None when the element is not found


# storage class for holding the non-zero matrix elements
class _MatrixElement:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
