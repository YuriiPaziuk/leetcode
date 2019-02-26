"""
You are given an integer array sorted in ascending order (may contain
duplicates), you need to split them into several subsequences, where
each subsequences consist of at least 3 consecutive integers. Return
whether you can make such a split.

Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3
3, 4, 5

Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3, 4, 5
3, 4, 5

Example 3:
Input: [1,2,3,4,4,5]
Output: False
"""
class Solution:

    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        groups = []
        for num in nums:
            if not groups:
                groups.append(list())
                groups[0].append(num)
            else:
                need_new_group = True
                # Groups that end with num-1
                t = [g for g in groups if g[-1] == num - 1]
                if t:
                    # Group with minimum length
                    t = min(t, key=lambda g: len(g))
                    need_new_group = False
                    t.append(num)
                if need_new_group:
                    groups.append(list())
                    groups[-1].append(num)
        return min(len(group) for group in groups) >= 3


def main():
    tests = [
        ([1,2,3,3,4,5], True),
        ([1,2,3,3,4,4,5,5], True),
        ([1,2,3,4,4,5], False)
    ]
    s = Solution()
    for data, result in tests:
        print(data, result, ' : ', s.isPossible(data))


if __name__ == '__main__':
    main()