"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sequences = []
        i = 0
        while i < len(nums):
            count = 0
            while i < len(nums) and nums[i]:
                count += 1
                i += 1
            if count:
                sequences.append(count)
            while i < len(nums) and not nums[i]:
                i += 1
        return max(sequences) if sequences else 0


class Solution2:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_all, max_local = 0, 0
        for i in nums:
            max_local = max_local + 1 if i else 0
            max_all = max(max_all, max_local)
        return max_all


class Solution3:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, count = 0, 0
        for num in nums:
            if num:
                count += 1
                result = max(result, count)
            else:  # i == 0
                count = 0
        return result


class Solution4:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, count = 0, 0
        for num in nums:
            count = (count + num) * num
            result = max(result, count)
        return result


def main():
    tests = [
        ([], 0),
        ([0], 0),
        ([1], 1),
        ([0, 1], 1),
        ([1, 0], 1),
        ([0, 0], 0),
        ([1, 1], 2),
        ([1, 0, 1], 1),
        ([1, 1, 0], 2),
        ([0, 1, 1], 2),
        ([1, 0, 1, 1], 2)
    ]
    for nums, max_ones in tests:
        assert Solution4().findMaxConsecutiveOnes(nums) == max_ones, nums


if __name__ == "__main__":
    main()