# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/


class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        nums = Counter(nums)
        if k < 0:
            return 0
        elif k == 0:
            return sum(1 for t in nums.values() if t > 1)
        else: # k > 0
            return sum(1 for t in nums if t + k in nums)


def main():
    tests = [
        ([3, 1, 4, 1, 5], 2, 2), # (1, 3) and (3, 5)
        ([1, 2, 3, 4, 5], 1, 4), # (1, 2), (2, 3), (3, 4) and (4, 5)
        ([1, 3, 1, 5, 4], 0, 1), # (1, 1)
        ([1,2,3,4,5], -1, 0)
    ]
    t = Solution()
    for nums, k, result in tests:
        assert t.findPairs(nums, k) == result, (nums, t.findPairs(nums, k))


if __name__ == '__main__':
    main()
