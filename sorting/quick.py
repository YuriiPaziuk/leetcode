def quick_sort(a):

    def partition(a, low, high):
        i, x = low, a[low]
        for j in range(low + 1, high + 1):
            if a[j] < x:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i], a[low] = a[low], a[i]
        return i

    def sort(a, low, high):
        if low < high:
            p = partition(a, low, high)
            sort(a, low, p - 1)
            sort(a, p + 1, high)

    sort(a, 0, len(a) - 1)


def main():
    a = [5, 7, 1, 6, 4, 8, 3, 2, 9]
    #print(partition(a, 0, len(a) - 1), a)
    quick_sort(a)
    print(a)


if __name__ == '__main__':
    main()