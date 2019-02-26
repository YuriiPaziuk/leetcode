"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        a = 1
        for x in reversed(digits):
            a, b = divmod(x + a, 10)
            result.append(b)
        if a: result.append(a)

        return result[::-1]

    def plusOne1(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                break
            digits[i] = 0
        return digits if digits[0] else [1] + digits


def main():
    tests = [
        ([0], [1]),
        ([0], [1]),
        ([1], [2]),
        ([9], [1, 0]),
        ([9, 9], [1, 0, 0]),
        ([1, 9], [2, 0]),
        ([1, 2], [1, 3])
    ]
    for digits, result in tests:
        print(result, Solution().plusOne(digits))


if __name__ == '__main__':
    main()
