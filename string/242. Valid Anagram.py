"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
class Solution:
    def isAnagram1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 112 ms
        return sorted(s) == sorted(t)

    def isAnagram2(self, s, t):
        # 99 ms
        d1, d2 = {}, {}
        for char in s:
            d1[char] = d1.get(char, 0) + 1
        for char in t:
            d2[char] = d2.get(char, 0) + 1
        return d1 == d2

    def isAnagram3(self, s, t):
        # 106 ms
        d1, d2 = [0] * 26, [0] * 26
        for char in s:
            d1[ord(char) - ord('a')] += 1
        for char in t:
            d2[ord(char) - ord('a')] += 1
        return d1 == d2

    def isAnagram3(self, s, t):
        # 69 ms
        from collections import Counter
        return Counter(s) == Counter(t)

    def isAnagram4(self, s, t):
        # 62 ms
        letters = "EARIOTNSLCUDPMHGBFYWKVXZJQ"
        for letter in letters:
            if s.count(letter) != t.count(letter): return False
        return True

    def isAnagram5(self, s, t):
        # 52 ms
        letters = set(s + t)
        for letter in letters:
            if s.count(letter) != t.count(letter): return False
        return True


def main():
    pass


if __name__ == '__main__':
    main()
