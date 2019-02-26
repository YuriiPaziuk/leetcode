# https://leetcode.com/problems/move-zeroes/description/

def moveZeroes(nums):
    left = right = 0
    while right < len(nums):
        # Find next nearest non-zero element
        while right < len(nums) and nums[right] == 0:
            right += 1
        # If there is next non-zero element, swap left and right
        if right < len(nums):
            nums[left], nums[right] = nums[right], nums[left]
        # Update pointers
        left += 1
        right += 1


def main():
    tests = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])
    ]
    for nums, result in tests:
        moveZeroes(nums)
        print(nums)
        #assert nums == result


if __name__ == '__main__':
    main()
