# https://leetcode.com/problems/length-of-last-word/description/


def lengthOfLastWord(s):
    if not s:
        return 0
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    if i == -1:
        return 0
    j = i - 1
    while j >= 0 and s[j] != ' ':
        j -= 1
    return i - j


def lengthOfLastWord(s):
    words = s.rstrip().split()
    return len(words[-1]) if words else 0


def main():
    tests = [
        ('', 0),
        ('a', 1),
        ('a a', 1),
        ('a aa', 2),
        ('a ', 1),
        ('aa aaa ', 3),
        (' ', 0)
    ]
    for s, result in tests:
        print(s, lengthOfLastWord(s))
        #assert result == lengthOfLastWord(s), s


if __name__ == '__main__':
    main()
