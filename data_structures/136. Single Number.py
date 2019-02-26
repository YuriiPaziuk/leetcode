"""
Given an array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        count = Counter(nums)
        for key, val in count.items():
            if val == 1: return key

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for num in nums:
            if num in s: s.discard(num)
            else: s.add(num)
        return s.pop()

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = nums[0]
        for num in nums[1:]:
            x ^= num
        return x


def main():
    tests = [
        ([1,2,3,1,2], 3)
    ]
    for nums, result in tests:
        print(nums, result, Solution().singleNumber(nums))


if __name__ == '__main__':
    main()
