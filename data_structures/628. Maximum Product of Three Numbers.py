# https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution:
    def maximumProduct(self, nums): # 68 ms
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        a = heapq.nsmallest(3, nums)
        b = heapq.nlargest(3, nums)
        return max(b[0] * b[1] * b[2], a[0] * a[1] * b[0])

    def maximumProduct(self, nums): # 108 ms
        s = sorted(nums)
        return max(s[-1] * s[-2] * s[-3], s[0] * s[1] * s[-1])


def main():
    tests = [
        ([1,2,3], 6),
        ([1,2,3,4], 24)
    ]
    sol = Solution()
    for nums, result in tests:
        assert result == sol.maximumProduct(nums), (nums, result, sol.maximumProduct(nums))


if __name__ == '__main__':
    main()
