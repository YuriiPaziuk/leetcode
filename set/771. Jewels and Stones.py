# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        result = 0
        j = set(J)
        for t in S:
            if t in j:
                result += 1
        return result


def main():
    tests = [
        ["aA", "aAAbbbb", 3],
        ["z", "ZZ", 0]
    ]
    sol = Solution()
    for j, s, result in tests:
        assert result == sol.numJewelsInStones(j, s), (j, s, result, sol.numJewelsInStones(j, s))


if __name__ == '__main__':
    main()
