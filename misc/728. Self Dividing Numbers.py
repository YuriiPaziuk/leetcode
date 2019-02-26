# https://leetcode.com/problems/self-dividing-numbers/description/


class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left, right + 1):
            if self.isSelfDividingNumber(i):
                result.append(i)
        return result

    def isSelfDividingNumber(self, num):
        t = num
        while t:
            if t % 10 == 0 or num % (t % 10) != 0:
                return False
            t //= 10
        return True


def main():
    tests = [
        [1, 22, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]]
    ]
    sol = Solution()
    for left, right, result in tests:
        assert result == sol.selfDividingNumbers(left, right), (result, sol.selfDividingNumbers(left, right))


if __name__ == '__main__':
    main()
