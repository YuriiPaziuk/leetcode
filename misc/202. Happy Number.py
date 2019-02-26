"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by
the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tortoise = self.digits_squares_sum(n)
        hare = self.digits_squares_sum(self.digits_squares_sum(n))
        while tortoise != hare:
            tortoise = self.digits_squares_sum(tortoise)
            hare = self.digits_squares_sum(self.digits_squares_sum(hare))
        return tortoise == 1

    def digits_squares_sum(self, x):
        if x == 1: return 1
        squares_sum = 0
        while x:
            squares_sum += (x % 10) ** 2
            x //= 10
        return squares_sum

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.f(n)
        return n == 1

    def f(self, x):
        if x < 10:
            return x ** 2
        else:
            return (x % 10) ** 2 + self.f(x // 10)


def main():
    for i in range(20):
        print(Solution().isHappy(i))


if __name__ == '__main__':
    main()
