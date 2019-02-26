"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
"""
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        result = count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
                result = max(result, count)
            else:
                count = 1
        return result


def main():
    tests = [
        ([1,3,5,4,7], 3),
        ([2,2,2,2,2], 1),
        ([], 0),
        ([1,3,5,4,2,3,4,5], 4)
    ]
    for nums, result in tests:
        print(Solution().findLengthOfLCIS(nums))

if __name__ == '__main__':
    main()