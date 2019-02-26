"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""
class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        count = 0
        while n >= i:
            n -= i
            i += 1
            count += 1
        return count


def f(n):
    """
    sum = (x + 1) * x / 2
    x = (-1 + sqrt(8 * n + 1)) / 2
    """
    import math
    return int(-1 + math.sqrt(1 + 8 * n)) // 2


def main():
    for n in range(10):
        print(n, Solution().arrangeCoins(n), f(n))


if __name__ == '__main__':
    main()