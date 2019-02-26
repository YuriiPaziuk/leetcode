def missing_number(nums):
    return len(nums) * (len(nums) + 1) / 2 - sum(nums)


def main():
    tests = [
        ([3,0,1], 2),
        ([9,6,4,2,3,5,7,0,1], 8)
    ]
    for nums, result in tests:
        assert result == missing_number(nums), nums


if __name__ == '__main__':
    main()
