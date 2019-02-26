# https://leetcode.com/problems/reverse-integer/description/


def reverse(x):
    x = str(x)
    if x[0] == '-':
        x = int('-' + x[1:][::-1])
    else:
        x = int(x[::-1])
    if x < -2147483648 or x > 2147483647:
        return 0
    else:
        return x


def main():
    tests = [
        [123, 321],
        [-123, -321],
        [120, 21]
    ]
    for x, result in tests:
        assert result == reverse(x), (x, result, reverse(x))


if __name__ == '__main__':
    main()
