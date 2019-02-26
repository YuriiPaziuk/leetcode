"""
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
def maj_elem_1(a):
    import collections
    c = collections.Counter(a)
    return c.most_common()[0][0]


def maj_elem_2(a):
    return sorted(a)[len(a) // 2]


def maj_elem_3(a):
    candidate, count = None, 0
    for x in a:
        if count == 0:
            candidate = x
        count += 1 if candidate == x else -1
    return candidate


def main():
    a = [1, 3, 2, 3, 3, 4, 3]
    me = 3
    print(maj_elem_3(a))


if __name__ == '__main__':
    main()