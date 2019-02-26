"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return list((i, j))


class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prev = {}
        for i, num in enumerate(nums):
            if target - num in prev:
                return list((min((i, prev[target - num])), max((i, prev[target - num]))))
            else:
                prev[num] = i
        return None


def main():
    tests = [
        ([2, 7, 11, 15], 9, [0, 1])
    ]
    for nums, target, result in tests:
        print(nums, target, result, Solution2().twoSum(nums, target))


if __name__ == '__main__':
    main()
