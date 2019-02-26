def findDisappearedNumbers(nums):
    all_nums = set(range(1, len(nums) + 1))
    return sorted(list(all_nums - set(nums)))


def findDisappearedNumbers(nums):
    for num in nums:
        nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]


def main():
    tests = [
        ([4,3,2,7,8,2,3,1], [5,6])
    ]
    for nums, result in tests:
        print(findDisappearedNumbers(nums))


if __name__ == '__main__':
    main()
