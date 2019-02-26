"""
Linear search: iterate through the array until you find the element you
are looking for. If you reach the end of the array and haven't yet found
the element, return not found.

Binary search: for a given sorted array nums and value x, find nums[i]==x,
otherwise the greatest i where nums[i]==x, otherwise (x < nums[low]) the
result is low - 1.
"""

def linear_search_iter(nums, x):
    """
    Given an unsorted array nums, find the smallest index i where
    nums[i] == x. If there is no such i, return None.

    :param nums:
    :param x:
    :return:
    """
    for i, num in enumerate(nums):
        if x == num:
            return i
    return None


def linear_search_rec(nums, low, high, x):
    """
    Recursive solution. Base case: 1) nums is empty, return None;
    2) match of the first element of the array, nums[low]==x,
    return low.
    :param nums: the array of values
    :param low: the lower bond in the array in which to search
    :param high: upper bound in the array in which to search
    :param x: the value for which to search
    :return: i if found nums[i]==x else None
    """
    if low == high:
        return None
    elif nums[low] == x:
        return low
    else:
        return linear_search_rec(nums, low+1, high, x)


def binary_search_rec(nums, low, high, x):
    """
    For a sorted array nums:
    1. return i if nums[i] == x
    2. if x not in nums return i such that nums[i] < x < nums[i+1]
        a. return -1 if x < nums[0]
        b. return len(nums)-1 if nums[-1] < x
    :param nums:
    :param low:
    :param high:
    :param x:
    :return:
    """
    if high < low:
        return low - 1
    mid = low + (high - low) // 2
    if x == nums[mid]:
        return mid
    elif x < nums[mid]:
        return binary_search_rec(nums, low, mid-1, x)
    else:
        return binary_search_rec(nums, mid+1, high, x)


def binary_search_iter(nums, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2
        if x == nums[mid]:
            return mid
        elif x < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low - 1


def test_linear_search():
    import random
    nof_tests = 1000
    nums_size = 0, 100
    nums_values = 0, 100
    for _ in range(nof_tests):
        current_size = random.randrange(*nums_size)
        nums = [random.randrange(*nums_values) for _ in range(current_size)]
        x = random.randrange(*nums_values)
        try:
            ls = linear_search_iter(nums, x)
            lsr = linear_search_rec(nums, 0, len(nums), x)
            if ls != lsr:
                print(nums, x, ls, lsr)
        except:
            print(nums, x)


def test_binary_search():
    import random
    nof_tests = 1000
    nums_size = 0, 100
    nums_values = 0, 100
    for _ in range(nof_tests):
        current_size = random.randrange(*nums_size)
        nums = sorted([random.randrange(*nums_values) for _ in range(current_size)])
        x = random.randrange(*nums_values)
        try:
            bsr = binary_search_rec(nums, 0, len(nums)-1, x)
            bsi = binary_search_iter(nums, 0, len(nums)-1, x)
            if bsr != bsi:
                print(nums, x, bsr, bsi)
        except:
            print(nums, x)


def main():
    test_linear_search()
    test_binary_search()


if __name__ == '__main__':
    main()