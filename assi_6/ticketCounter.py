import random
import ctypes


class Array:
    # Creates an array with size elements.
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element.
        self.clear(None)
        # Returns the size of the array.

    def __len__(self):
        return self._size

    # Gets the contents of the index element.
    def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[index]

    # Puts the value in the array element at index position.
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[index] = value

    # Clears the array by setting each element to the given value.
    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    # Returns the array's iterator for traversing the elements.
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


# Implementation of the Queue ADT using a linked list.
class Queue:
    # Creates an empty queue.
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0

    # Returns True if the queue is empty.
    def isEmpty(self):
        return self._qhead is None

    # Returns the number of items in the queue.
    def __len__(self):
        return self._count

    # Adds the given item to the queue.
    def enqueue(self, item):
        node = _QueueNode(item)
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node
        self._qtail = node
        self._count += 1

    # Removes and returns the first item in the queue.
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._count -= 1
        return node.item


# Private storage class for creating the linked list nodes.
class _QueueNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None


# Used to store and manage information related to an airline passenger.
class Passenger:
    # Creates a passenger object.
    def __init__(self, idNum, arrivalTime):
        self._idNum = idNum
        self._arrivalTime = arrivalTime

    # Gets the passenger's id number.
    def idNum(self):
        return self._idNum

    # Gets the passenger's arrival time.
    def timeArrived(self):
        return self._arrivalTime

    # Used to store and manage information related to an airline ticket agent.


class TicketAgent:
    # Creates a ticket agent object.
    def __init__(self, idNum):
        self._idNum = idNum
        self._passenger = None
        self._stopTime = -1

    # Gets the ticket agent's id number.
    def idNum(self):
        return self._idNum

    # Determines if the ticket agent is free to assist a passenger.
    def isFree(self):
        return self._passenger is None

    # Determines if the ticket agent has finished helping the passenger.
    def isFinished(self, curTime):
        return self._passenger is not None and self._stopTime == curTime

    # Indicates the ticket agent has begun assisting a passenger.
    def startService(self, passenger, stopTime):
        self._passenger = passenger
        self._stopTime = stopTime

    # Indicates the ticket agent has finished helping the passenger.
    def stopService(self):
        thePassenger = self._passenger
        self._passenger = None
        return thePassenger


class TicketCounterSimulation:  # Create a simulation object.
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
        # Simulation components.
        self._passengerQ = Queue()
        self._theAgents = Array(numAgents)
        for i in range(numAgents):
            self._theAgents[i] = TicketAgent(i + 1)
        # self._theAgents = []
        # for i in range( numAgents ) :
        #     self._theAgents.append(TicketAgent(i+1))

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    # Run the simulation using the parameters supplied earlier.
    def run(self):
        for curTime in range(self._numMinutes + 1):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)

    # Print the simulation results.
    def printResults(self):
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed / 60
        print("")
        print("Number of passengers served = ", numServed)
        print("Number of passengers remaining in line = %d" % len(self._passengerQ))
        print("The average wait time was %4.2f minutes." % avgWait)

    # Rule 1: If a customer arrives, he is added to the queue.
    # At most, one customer can arrive during each time step.
    def _handleArrival(self, curTime):

        rnd = random.uniform(0, 1)
        if rnd <= self._arriveProb:
            self._numPassengers += 1
            p = Passenger(self._numPassengers, curTime)
            self._passengerQ.enqueue(p)

    # Rule 2: If there are customers waiting, for each free server,
    # the next customer in line begins her transaction.
    def _handleBeginService(self, curTime):
        for agent in self._theAgents:
            if agent.isFree() and (not self._passengerQ.isEmpty()):
                p = self._passengerQ.dequeue()
                agent.startService(p, curTime + self._serviceTime)
                self._totalWaitTime += curTime - p.timeArrived()

    # Rule 3: For each server handling a transaction,
    # if the transaction is complete, the customer departs and the server becomes free.
    def _handleEndService(self, curTime):
        for agent in self._theAgents:
            if agent.isFinished(curTime):
                agent.stopService()


if __name__ == "__main__":
    random.seed(4500)
    numMinutes = 10000 * 60
    numAgents = 3
    betweenTime = 2 * 60
    serviceTime = 4 * 60
    sim = TicketCounterSimulation(numAgents, numMinutes, betweenTime, serviceTime)
    sim.run()
    sim.printResults()
