"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first
4
 to
1
 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2: return True
        modified = False
        if nums[0] > nums[1]:
            nums[0] = nums[1]
            modified = True
        for i in range(2, len(nums)):
            if nums[i-2] <= nums[i-1] <= nums[i]: continue
            if modified:
                return False
            else:
                modified = True
                if nums[i-2] <= nums[i]: nums[i-1] = nums[i]
                else: nums[i] = nums[i-1]
        return True

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n <= 2:
            return True

        strike = 0 if nums[0] > nums[1] else 1
        for i in range(2, len(nums)):
            if nums[i] >= nums[i-1]:
                pass
            else:
                if nums[i] >= nums[i-2]: # Still Chance
                    strike -= 1
                    nums[i-1] = nums[i-2]
                else:
                    nums[i] = nums[i-1]
                    strike -= 1
                if strike < 0: return False
        return True


def main():
    tests = [
        ([4,2,3], True),
        ([4,2,1], False),
        ([3,4,2,3], False),
        ([3,4,2,3], False),
        ([3,1], True)
    ]
    for nums, result in tests:
        print(nums, result, Solution().checkPossibility(nums))

if __name__ == '__main__':
    main()
