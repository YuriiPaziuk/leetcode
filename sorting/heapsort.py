def heap_sort(a):

    parent      = lambda i: (i - 1) // 2
    left_child  = lambda i: 2 * i + 1
    right_child = lambda i: 2 * i + 2

    def sift_up(a, i):
        while i > 0 and a[parent(i)] < a[i]:
            a[parent(i)], a[i] = a[i], a[parent(i)]
            i = parent(i)

    def sift_down(a, i, size):
        max_index = i
        left = left_child(i)
        if left < size and a[left] > a[max_index]:
            max_index = left
        right = right_child(i)
        if right < size and a[right] > a[max_index]:
            max_index = right
        if i != max_index:
            a[i], a[max_index] = a[max_index], a[i]
            sift_down(a, max_index, size)

    def heapify(a):
        """Transform a list a into a heap"""
        for i in range(len(a) // 2, -1, -1):
            sift_down(a, i, len(a))

    # Main sorting procedure
    heapify(a)
    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        sift_down(a, 0, i)


def main():
    tests = [
        [],
        [11],
        [11, 22],
        [22, 11],
        [11, 33, 22],
        [11, 22, 33]
    ]
    for a in tests:
        heap_sort(a)
        print(a)
    a = [1,3,5,2,4,6,7,9,8]
    heap_sort(a)
    print(a)


if __name__ == '__main__':
    main()