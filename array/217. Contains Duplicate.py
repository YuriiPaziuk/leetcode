def containsDuplicates(nums):
    return len(set(nums)) != len(nums)


def main():
    tests = [
        ([], False),
        ([11], False),
        ([11, 22], False),
        ([11, 11], True),
        ([11, 22, 33], False),
        ([11, 22, 11], True)
    ]
    for nums, result in tests:
        assert result == containsDuplicates(nums), nums


if __name__ == '__main__':
    main()
