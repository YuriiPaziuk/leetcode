# https://leetcode.com/problems/valid-perfect-square/description/

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in range(1, num):
            if i ** 2 == num:
                return True
        return False

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 1, num
        while left + 1 < right:
            mid = left + (right - left) // 2
            square = mid ** 2
            if square == num:
                return True
            elif square > num:
                left = mid
            else:
                right = mid
        return (left + 1) ** 2 == num


def main():
    tests = [
        (16, True),
        (14, False)
    ]
    t = Solution()
    for num, result in tests:
        assert result == t.isPerfectSquare(num), (num, t.isPerfectSquare(num))


if __name__ == '__main__':
    main()
