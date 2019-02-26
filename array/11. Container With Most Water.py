"""
Given n non-negative integers a1, a2, ..., an, where each represents
a point at coordinate (i, ai). n vertical lines are drawn such that
the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
which together with x-axis forms a container, such that the container
contains the most water.

Note: You may not slant the container and n is at least 2.
"""
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        result = left, right, (right - left) * min(height[left], height[right])
        while left < right:
            temp = (right - left) * min(height[left], height[right])
            if temp > result[2]:
                result = left, right, temp
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result


def main():
    """import random
    nof_tests = 100
    nums_size = 2, 5  # min max
    nums_values = 1, 10  # min max
    for _ in range(nof_tests):
        current_size = random.randrange(*nums_size)
        nums = [random.randrange(*nums_values) for _ in range(current_size)]
        print(nums, Solution().maxArea(nums))
    """
    tests = [
        ([2,3,4,5,18,17,6], 17)
    ]
    for nums, result in tests:
        print(nums, result, Solution().maxArea(nums))


if __name__ == '__main__':
    main()