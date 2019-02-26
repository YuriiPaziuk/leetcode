parent      = lambda i: (i - 1) // 2
left_child  = lambda i: 2 * i + 1
right_child = lambda i: 2 * i + 2

def sift_up(a, i):
    while i > 0 and a[parent(i)] < a[i]:
        a[parent(i)], a[i] = a[i], a[parent(i)]
        i = parent(i)


def sift_down(a, i):
    max_index = i
    left = left_child(i)
    if left < len(a) and a[left] > a[max_index]:
        max_index = left
    right = right_child(i)
    if right < len(a) and a[right] > a[max_index]:
        max_index = right
    if i != max_index:
        a[i], a[max_index] = a[max_index], a[i]
        sift_down(a, max_index)


def heapify(a):
    """Transform a list a into a heap"""
    for i in range(len(a) // 2, -1, -1):
        sift_down(a, i)


def heap_push(heap, item):
    heap.append(item)
    sift_up(heap, len(heap) - 1)


def heap_pop(heap):
    result = heap[0]
    if len(heap) > 1:
        heap[0] = heap.pop()
        sift_down(heap, 0)
    else:
        heap.pop()
    return result



def main():
    """a = []
    for i in range(1, 10):
        heap_push(a, i)
        print(a)
    while a:
        print(heap_pop(a))
    a = [1,3,5,2,4,6,7,9,8]
    heapify(a)
    print(a)"""
    a = [1,3,5,2,4,6,7,9,8]
    print(a)


if __name__ == '__main__':
    main()