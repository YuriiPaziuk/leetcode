"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 1:

Input: [1,3,5,6], 0
Output: 0

https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

"""
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #return self.pos(nums, target, 0, len(nums))

        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            m = (lo + hi) // 2
            if nums[m] == target: return m
            lo, hi = (lo, m - 1) if nums[m] > target else (m + 1, hi)
        return lo



    def pos(self, nums, target, left, right):
        if left >= right:
            return left
        else:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                return self.pos(nums, target, middle + 1, right)
            else:  # nums[middle] > target
                return self.pos(nums, target, left, middle - 1)


def main():
    tests = [
        ([1,3,5,6], 5, 2),
        ([1,3,5,6], 2, 1),
        ([1,3,5,6], 0, 0),
        ([], 1, 0),
        ([1, 3], 2, 1)
    ]
    for nums, target, position in tests[:]:
        print(nums, target, position, Solution().searchInsert(nums, target))


if __name__ == '__main__':
    main()
