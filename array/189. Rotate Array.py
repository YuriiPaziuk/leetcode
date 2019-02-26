# https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]


def main():
    tests = [
        ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4])    
    ]
    t = Solution()
    for nums, k, result in tests:
        assert t.rotate(nums, k) == result, (nums, t.rotate(nums, k))


if __name__ == '__main__':
    main()
