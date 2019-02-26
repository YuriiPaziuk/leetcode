# https://leetcode.com/problems/first-unique-character-in-a-string/description/


def firstUniqChar(s):
    for i, c in enumerate(s):
        if s.count(c) == 1:
            return i
    return -1


def firstUniqChar(s):
    from collections import Counter
    cnt = Counter(s)
    for i, c in enumerate(s):
        if cnt.get(c, 0) == 1:
            return i
    return -1


def firstUniqChar(s):
    from collections import OrderedDict
    from itertools import islice

    unique_elems = OrderedDict()
    non_unique_elems = set()

    for i, c in enumerate(s):
        if c in unique_elems:
            del unique_elems[c]
            non_unique_elems.add(c)
        if c not in non_unique_elems:
            unique_elems[c] = i
    
    return next(islice(unique_elems.values(), 0, 1))


def main():
    tests = [
        ("leetcode", 0),
        ("loveleetcode", 2)
    ]
    for s, result in tests:
        print(firstUniqChar(s))


if __name__ == '__main__':
    main()
