"""
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want
to return an integer, the decimal part will be truncated.
"""
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        err = 0.1
        left, right = 1, x
        middle = left + (right - left) / 2

        while not x < middle * middle < x + err:
            if middle * middle > x:
                right = middle - 1
            else:
                left = middle + 1
            middle = left + (right - left) / 2
        return int(middle)


def main():
    import math
    for x in range(26):
        print(x, math.sqrt(x), Solution().mySqrt(x))
    print(46339, Solution().mySqrt(2147395599))


if __name__ == '__main__':
    main()