# https://leetcode.com/problems/ransom-note/description/


def canConstruct(ransomNote, magazine):
    from collections import Counter
    r, m = Counter(ransomNote), Counter(magazine)
    return not r - m  # smaller Counter - bigger Counter


def canConstruct(ransomNote, magazine):
    return all(magazine.count(x) >= ransomNote.count(x) for x in set(ransomNote))


def main():
    tests = [
        ('a', 'b', False),
        ('aa', 'ab', False),
        ('aa', 'aba', True)
    ]
    for ransomNote, magazine, result in tests:
        print(canConstruct(ransomNote, magazine))


if __name__ == '__main__':
    main()
