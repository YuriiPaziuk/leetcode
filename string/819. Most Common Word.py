# https://leetcode.com/problems/most-common-word/description/


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import collections
        import re
        banned = set(banned)
        t = re.split('\W+', paragraph)
        t = collections.Counter(i.lower() for i in t if i.lower() not in banned)
        return t.most_common(1)[0][0]


def main():
    tests = [
        ["Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"], "ball"]
    ]
    t = Solution()
    for paragraph, banned, result in tests:
        assert t.mostCommonWord(paragraph, banned) == result, (paragraph, t.mostCommonWord(paragraph, banned))


if __name__ == '__main__':
    main()
