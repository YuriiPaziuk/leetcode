"""
Given a list of non negative integers, arrange them such that they form the largest number.
For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
Note: The result may be very large, so you need to return a string instead of an integer.
"""
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key

        def cmp(x, y):
            a, b = x + y, y + x
            if   a > b:  return  1
            elif a == b: return  0
            else:        return -1

        nums = [str(x) for x in nums]
        nums.sort(key=cmp_to_key(cmp), reverse=True)
        return ''.join(nums).lstrip('0') or '0'


def main():
    tests = [
        ([3, 30, 34, 5, 9], 9534330)
    ]
    for nums, result in tests:
        print(nums, result, Solution().largestNumber(nums))


if __name__ == '__main__':
    main()
