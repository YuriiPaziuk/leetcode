"""
Algorithm.
1. Find the minimum element of the array.
2. Swap it with the first element of the array.
3. Repeat with the remaining part of the array.
"""
def selection_sort(a):
    if a:
        i = a.index(min(a))
        a[0], a[i] = a[i], a[0]
        selection_sort(a[1:])


def selection_sort_iter(a):
    for i in range(len(a)):
        idx = a.index(min(a[i:]), i)
        a[i], a[idx] = a[idx], a[i]


def main():
    a = [4, 2, 1, 3, 5]
    selection_sort_iter(a)
    print(a)


if __name__ == '__main__':
    main()