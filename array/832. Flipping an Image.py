# https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[1 ^ t for t in row[::-1]] for row in A]


def main():
    tests = [
        [[[1,1,0],[1,0,1],[0,0,0]], [[1,0,0],[0,1,0],[1,1,1]]],
        [[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]], [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]]
    ]
    s = Solution()
    for input, output in tests:
        assert output == s.flipAndInvertImage(input), (input, output, s.flipAndInvertImage(input))


if __name__ == '__main__':
    main()
