# https://leetcode.com/problems/perfect-number/description/


class Solution:
    checkPerfectNumber2 = {6, 28, 496, 8128, 33550336, 8589869056}.__contains__

    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1: return False
        from math import sqrt
        s, SQRT = 1, int(sqrt(num))
        for i in range(2, SQRT + 1):
            if num % i == 0:
                s += i + num // i
        return s == num


    def checkPerfectNumber1(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s = 0
        t = 1
        while t < num:
            if num % t == 0:
                s += t
            if s > num:
                return False
            t += 1
        return s == num


def main():
    tests = [6, 28, 496, 8128, 33550336, 8589869056]
    sol = Solution()
    for num in tests:
        assert sol.checkPerfectNumber(num), (num, sol.checkPerfectNumber((num)))


if __name__ == '__main__':
    main()
