class SinglyLinkedList:

    class Node:

        def __init__(self, data, next=None):
            self._data = data
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def empty(self):
        return self._head == None

