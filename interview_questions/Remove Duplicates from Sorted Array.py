# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':

        if len(nums) < 2:
            return len(nums)

        left, right = 0, 0
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            right += 1

        return left + 1


def main():
    tests = [
        ([], 0),
        ([1], 1),
        ([1,1,2], 2),
        ([0,0,1,1,1,2,2,3,3,4], 5)
    ]
    for nums, answer in tests:
        print(nums, Solution().removeDuplicates(nums), nums)


if __name__ == '__main__':
    main()
