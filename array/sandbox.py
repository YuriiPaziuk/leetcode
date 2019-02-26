def count01(nums):
    """
    Count number of 0 and 1 in an array, that consists only
    of 0 and 1.
    :param nums: list(int) of 0 and 1
    :return: (nof_0, nof_1)
    """
    #return len(nums) - sum(nums), sum(nums)
    return nums.count(0), nums.count(1)


def separate0and1(nums):
    """
    Return a new array with 0 at the beginning and ones at
    the end.
    :param nums: list(int) of 0 and 1
    :return: list(int)
    """
    nof_0, nof_1 = count01(nums)
    return [0] * nof_0 + [1] * nof_1


def convertto10(nums):
    """
    Array of 0 and 1 represents a binary number. Convert it
    to the decimal form.
    :param nums: list(int) of 0 and 1.
    :return: int
    """
    result = 0
    for i, num in enumerate(reversed(nums)):
        result += num * 2 ** i
    return result


def f(a):
    a.clear()
    a.extend([11, 22])


def main():
    tests = [
        ([], (0,0), [], 0),
        ([0], (1,0), [0], 0),
        ([1], (0,1), [1], 1),
        ([0,1], (1,1), [0,1], 1),
        ([1,1], (0,2), [1,1], 3),
        ([1,0,1], (1,2), [0,1,1], 5)
    ]
    #for nums, f1, f2, f3 in tests:
    #    print(nums, count01(nums), separate0and1(nums), convertto10(nums))
    b = [33, 44, 55]
    f(b)
    print(b)


if __name__ == '__main__':
    main()