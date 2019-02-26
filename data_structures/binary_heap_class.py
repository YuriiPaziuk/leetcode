"""Max heap"""
class MaxHeap:

    def __init__(self):
        self.a = []
        self.parent      = lambda i: (i - 1) // 2
        self.left_child  = lambda i: 2 * i + 1
        self.right_child = lambda i: 2 * i + 2

    def sift_up(self, i):
        while i > 0 and self.a[self.parent(i)] < self.a[i]:
            self.a[self.parent(i)], self.a[i] = self.a[i], self.a[self.parent(i)]
            i = self.parent(i)

    def sift_down(self, i):
        max_index = i
        left = self.left_child(i)
        if left < len(self.a) and self.a[left] > self.a[max_index]:
            max_index = left
        right = self.right_child(i)
        if right < len(self.a) and self.a[right] > self.a[max_index]:
            max_index = right
        if i != max_index:
            self.a[i], self.a[max_index] = self.a[max_index], self.a[i]
            self.sift_down(max_index)

    def heapify(self):
        for i in range(len(self.a) // 2, -1, -1):
            self.sift_down(i)

    def push(self, item):
        self.a.append(item)
        self.sift_up(len(self.a) - 1)

    def heap_pop(self):
        result = self.a[0]
        if len(self.a) > 1:
            self.a[0] = self.a.pop()
            self.sift_down(0)
        else:
            self.a.pop()
        return result

    def remove(self, item):
        self.a.remove(item)
        self.heapify()

    def peek_max(self):
        return self.a[0]

    def empty(self):
        return len(self.a) == 0

    def __repr__(self):
        return self.a.__repr__()


def main():
    heap = MaxHeap()
    for x in [2,3,5,6,7,9,1,4,8]:
        heap.push(x)
    print(heap)
    while not heap.empty():
        print(heap.peek_max())
        heap.remove(heap.peek_max())
    print(heap)


if __name__ == '__main__':
    main()