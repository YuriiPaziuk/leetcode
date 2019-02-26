"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""
class Solution:
    def canJump(self, nums):
        """
        Return True if can reach the last element of nums,
        current_position + best_move >= len(nums) - 1
        Return False:
        If nums(current_position) == 0, unless nums=[0]
        :type nums: List[int]
        :rtype: bool
        """
        i = 0  # current position
        while i < len(nums):
            if i + nums[i] >= len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
            max_step = max(nums[i + 1: i + nums[i] + 1])
            idx = 0
            for idx in range(i + nums[i], i, -1):
                if nums[idx] == max_step:
                    break

            if nums[idx] >= nums[i] or nums[i + nums[i]] == 0:
                i = idx
            else:
                i = i + nums[i]
        return False


def main():
    tests = [
        ([2,3,1,1,4], True),
        ([3,2,1,0,4], False),
        ([1,1,0,1], False),
        ([1,1,1,1], True),
        ([5,9,3,2,1,0,2,3,3,1,0,0], True),
        ([4,2,0,0,1,1,4,4,4,0,4,0], True),
        ([1,1,2,2,0,1,1], True),
        ([5,9,3,2,1,0,2,3,3,1,0,0], True)
    ]
    for nums, result in tests[:]:
        assert Solution().canJump(nums) == result, nums


if __name__ == '__main__':
    main()