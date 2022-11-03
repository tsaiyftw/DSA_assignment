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


# start to count the number of each letter's occurance in the text file
theCounter = myArray(127)
theCounter.clear(0)
thefile = open("abc.txt", "r")
for line in thefile:
    for letter in line:
        code = ord(letter)
        theCounter[code] += 1
thefile.close()

# a 97
# e 101
# i 105
# 0 111
# u 117
lst = [97, 101, 105, 111, 117]
for item in lst:
    print("%c-%3d" % (chr(item), theCounter[item]))

# uppercase letter: 65~90 in ASCII
# lowercase letter: 97~122 in ASCII
for i in range(26):
    print(
        "%c-%4d; %c-%3d"
        % (chr(65 + i), theCounter[65 + i], chr(97 + i), theCounter[97 + i])
    )
