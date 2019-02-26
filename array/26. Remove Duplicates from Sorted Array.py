"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j + 1


class Solution2:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1 if nums else 0
        for num in nums:
            if num != nums[i-1]:
                nums[i] = num
                i += 1
        return i


def main():
    tests = [
        ([], 0),
        ([1], 1),
        ([1, 2], 2),
        ([1, 1], 1),
        ([1, 1, 2], 2),
        ([1, 2, 2], 2),
        ([1, 2, 2, 3, 3, 3], 3)
    ]
    for nums, max_ones in tests:
        assert Solution3().removeDuplicates(nums) == max_ones, (nums, max_ones)


if __name__ == "__main__":
    main()
