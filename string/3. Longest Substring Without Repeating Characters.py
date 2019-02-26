# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s):
        result = ''
        i, j = 0, 0
        t = ''
        while j < len(s):
            if s[j] not in t:
                t += s[j]
                j += 1
                if len(t) > len(result):
                    result = t
            else:
                if len(t) > len(result):
                    result = t
                i += 1
                j = i
                t = ''
        return result


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = ''
        i, j = 0, 0
        t = set()
        while j < len(s):
            if s[j] not in t:
                t.add(s[j])
                j += 1
                if j - i > len(result):
                    result = s[i:j]
            else:
                if j - i > len(result):
                    result = s[i:j]
                while s[j] in t:
                    t.discard(s[i])
                    i += 1
                t.add(s[j])
                j += 1
        return result


def main():
    tests = [
        #('abcabcbb', 'abc'),
        #('bbbbb', 'b'),
        #('pwwkew', 'wke'),
        ('au', 'au')
    ]
    x = Solution()
    for s, result in tests:
        assert x.lengthOfLongestSubstring(s) == result, (s, x.lengthOfLongestSubstring(s))


if __name__ == '__main__':
    main()
