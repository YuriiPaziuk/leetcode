def containsDuplicates(nums, k):
    d = {}
    for i, x in enumerate(nums):
        if x not in d:
            d[x] = i
        else:
            if i - d[x] <= k:
                return True
            else:
                d[x] = i
    return False


def main():
    tests = [
        ([], 1, False),
        ([11], 1, False),
        ([11, 22], 1, False),
        ([11, 11], 1, True),
        ([11, 22, 33], 2, False),
        ([11, 22, 11], 1, False),
        ([11, 22, 11], 2, True)
    ]
    for nums, k, result in tests:
        assert result == containsDuplicates(nums, k), nums


if __name__ == '__main__':
    main()
