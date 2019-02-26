# https://leetcode.com/problems/hamming-distance/description/


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y)[2:].count('1')


def main():
    tests = [
        [1, 4, 2]
    ]
    sol = Solution()
    for x, y, result in tests:
        assert result == sol.hammingDistance(x, y), (x, y, result, sol.hammingDistance(x, y))


if __name__ == '__main__':
    main()
