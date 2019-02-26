# https://leetcode.com/problems/implement-strstr/description/


def strStr(haystack, needle):
    len_haystack, len_needle = len(haystack), len(needle)
    if len_needle == 0:
        return 0
    for i in range(len_haystack - len_needle + 1):
        if haystack[i:i + len_needle] == needle:
            return i
    return -1


def main():
    tests = [
        ['a', '', 0],
        ['hello', 'll', 2],
        ['aaa', 'bcd', -1],
        ['mississippi', 'pi', 9]
    ]
    for haystack, needle, result in tests[3:]:
        assert result == strStr(haystack, needle), (haystack, needle, result, strStr(haystack, needle))


if __name__ == '__main__':
    main()
