# https://leetcode.com/problems/longest-palindrome/description/

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        c = Counter(s)
        max_len = 0
        for t in c:
            while c[t] >= 2:
                max_len += 2
                c[t] -= 2
        for t in c:
            if c[t] == 1:
                max_len += 1
                break
        return max_len

    def longestPalindrome(self, s):
        chars = set(s)
        max_len = 0
        plus_one = False
        for c in chars:
            cnt = s.count(c)
            if cnt % 2 == 0:
                max_len += cnt
            elif cnt >= 3:
                max_len += cnt - 1
                plus_one = True
            elif cnt == 1:
                plus_one = True
        return max_len + (1 if plus_one else 0)


def main():
    tests = [
        ("abccccdd", 7)
    ]
    sol = Solution()
    for s, res in tests:
        assert res == sol.longestPalindrome(s), (s, res, sol.longestPalindrome(s))


if __name__ == '__main__':
    main()
