# https://leetcode.com/problems/add-binary/description/


def addBinary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]


def main():
    tests = [
        ('11', '1', '100')
    ]
    for a, b, result in tests:
        print(addBinary(a, b))


if __name__ == '__main__':
    main()
