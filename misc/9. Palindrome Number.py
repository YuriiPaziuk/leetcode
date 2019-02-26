# https://leetcode.com/problems/palindrome-number/description/


def isPalindrome1(x):
    x = str(x)
    return x == x[::-1]


def isPalindrome(x):
    if x < 0: return False
    rev, xx = 0, x
    while xx > 0:
        rev = rev * 10 + xx % 10
        xx //= 10
    return rev == x


def main():
    tests = [
        [121, True],
        [-121, False],
        [10, False]
    ]
    for x, result in tests:
        assert result == isPalindrome(x), (x, result, isPalindrome(x))


if __name__ == '__main__':
    main()
