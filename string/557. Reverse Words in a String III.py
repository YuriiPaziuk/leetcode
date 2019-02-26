# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/


def reverseWords(s):
    return ' '.join(word[::-1] for word in s.split())


def main():
    tests = [
        ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc")
    ]
    for s, result in tests:
        assert result == reverseWords(s)


if __name__ == '__main__':
    main()
