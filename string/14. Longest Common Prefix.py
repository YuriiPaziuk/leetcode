# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        shortest_str = min(strs, key=lambda x: len(x))
        n = len(shortest_str)
        for str in strs:
            i = 0
            while i < n and str[i] == shortest_str[i]:
                i += 1
            n = i
            if i == 0:
                break
        return shortest_str[:n]


def main():
    tests = [
        (["flower","flow","flight"], "fl"),
        (["dog","racecar","car"], "")
    ]
    t = Solution()
    for strs, result in tests:
        assert t.longestCommonPrefix(strs) == result, (strs, result, t.longestCommonPrefix(strs))


if __name__ == '__main__':
    main()
