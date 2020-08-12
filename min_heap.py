# Course: CS261 - Data Structures
# Assignment: 5
# Student: Jeff Stone - - 934256195
# Description: This program implements a MinHeap class by implementing
# the following methods:
# add()
# get_min()
# remove_min()
# build_heap()



# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def parent(self, index):
        """
        This method sets the parent of a node
        :param: index of the node
        :return: returns the computed elements parental index
        """
        return (index - 1) // 2

    def left(self, index):
        """
        This method moves element to the left
        :param index: the index of the element
        :return: stores the element left
        """
        return 1 + index*2

    def right(self, index):
        """
        This method moves element to the right
        :param index: the index of the element
        :return: stores the element right
        """
        return 2 + index*2

    def to_root(self, i):
        """
        This method "bubbles up" the heap from an index to the root
        :param i: the current position as we iterate up the heap
        """
        while i > 0:
            if self.heap.get_at_index(i) < self.heap.get_at_index(self.parent(i)):
                self.heap.swap(i, self.parent(i))
            i = self.parent(i)

    def to_leaf(self, i):
        """
        This method "percolates down" the heap from an index to the leaf
        :param i: the current position as we iterate down the heap
        """
        while i < self.heap.length():
            left = self.left(i)
            right = self.right(i)

            # determines if next element goes left or right
            child = None
            val = self.heap.get_at_index(i)
            if left < self.heap.length() and val > self.heap.get_at_index(left):
                child = left
                val = self.heap.get_at_index(left)
            if right < self.heap.length() and val > self.heap.get_at_index(right):
                child = right
                val = self.heap.get_at_index(right)

            if child is not None:
                self.heap.swap(i, child)
                i = child

            else:
                break

    def add(self, node: object) -> None:
        """
        This method adds a new object to the MinHeap maintaining heap property.
        Runtime complexity of this implementation is O(logN).
        :param node: the object added to the MinHeap
        """
        self.heap.append(node)
        self.to_root(self.heap.length() - 1)

    def get_min(self) -> object:
        """
        This method returns an object with a minimum key without removing it from the heap.
        If the heap is empty, the method raises a MinHeapException.
        Runtime complexity of this implementation is O(1).
        :return: returns an object with a min key
        """
        if self.is_empty():
            raise MinHeapException()

        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        This method returns an object with a minimum key and removes it from the heap.
        If the heap is empty, the method raises a MinHeapException.
        Runtime complexity of this implementation is O(logN).
        :return: returns an object with a min key that is removed from heap
        """
        if self.is_empty():
            raise MinHeapException()
        val = self.heap.get_at_index(0)
        lastval = self.heap.pop()

        if self.heap.length() == 0:
            return val

        self.heap.set_at_index(0, lastval)
        self.to_leaf(0)

        return val

    def build_heap(self, da: DynamicArray) -> None:
        """
        This method receives a dynamic array with objects in any order
        and builds a proper MinHeap from them.
        The current content of the MinHeap is lost.
        Runtime complexity of this implementation is O(N).
        """
        self.heap = DynamicArray()
        for i in range(da.length()):
            self.add(da.get_at_index(i))


# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
