# https://leetcode.com/problems/longest-increasing-subsequence/description/

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best_count = 0
        for i in range(len(nums)):
            t = nums[i]
            count = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > t:
                    t = nums[j]
                    count += 1
            if count > best_count:
                best_count = count
        return best_count


def main():
    tests = [
        #[[10,9,2,5,3,7,101,18], 4],
        [[10,9,2,5,3,4], 3]
    ]
    s = Solution()
    for nums, n in tests:
        assert n == s.lengthOfLIS(nums), (nums, s.lengthOfLIS(nums))


if __name__ == '__main__':
    main()
