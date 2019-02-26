# https://leetcode.com/problems/number-of-segments-in-a-string/description/


def countSegments(s):
    return len(s.strip().split())


def main():
    tests = [
        ('', 0),
        (' ', 0,),
        ('aa', 1),
        ('  aa ', 1),
        ('a bb', 2),
        ('a bb   ccc  ', 3)
    ]
    for s, result in tests:
        print(countSegments(s))


if __name__ == '__main__':
    main()
