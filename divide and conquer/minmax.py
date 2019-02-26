def minmax_iter(nums):
    """
    Find both minimum and maximum in an array.
    :param nums:
    :return:
    """
    min_val, max_val = nums[0], nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val


def minmax_rec(nums, low, high):
    if low == high:
        return nums[low], nums[high]
    elif high - low == 1:
        return min(nums[low], nums[high]), max(nums[low], nums[high])
    else:
        mid = (low + high) // 2
        x1, y1 = minmax_rec(nums, low, mid)
        x2, y2 = minmax_rec(nums, mid + 1, high)
        return min(x1, x2), max(y1, y2)


def test_minmax():
    import random
    nof_tests = 1000
    nums_size = 1, 100
    nums_values = 0, 100
    for _ in range(nof_tests):
        current_size = random.randrange(*nums_size)
        nums = sorted([random.randrange(*nums_values) for _ in range(current_size)])
        x = random.randrange(*nums_values)
        try:
            mmi = minmax_iter(nums)
            mmr = minmax_rec(nums, 0, len(nums)-1)
            if mmi != mmr:
                print(nums, mmi, mmr)
        except:
            print(nums)


def main():
    test_minmax()


if __name__ == '__main__':
    main()