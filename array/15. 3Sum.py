"""
Given an array S of n integers, are there elements a, b, c
in S such that a + b + c = 0? Find all unique triplets in
the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    result.append(list((nums[i], nums[left], nums[right])))
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:  # s > 0:
                    right -= 1
        return result


def main():
    tests = [
        ([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]]),
        ([0,0,0], [[0,0,0]])
    ]
    for nums, result in tests:
        print(nums, Solution().threeSum(nums))


if __name__ == '__main__':
    main()