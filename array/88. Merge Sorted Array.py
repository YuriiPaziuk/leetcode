'''
Merge two sorted array into one.
'''
def merge(nums1, nums2):
    return sorted(nums1 + nums2)


def merge(nums1, nums2):
    result = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    result.extend(nums1[i:])
    result.extend(nums2[j:])
    return result


def merge(nums1, nums2):
    result = [0] * (len(nums1) + len(nums2))
    k = len(result) - 1
    i = len(nums1) - 1
    j = len(nums2) - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            result[k] = nums1[i]
            i -= 1
        else:
            result[k] = nums2[j]
            j -= 1
        k -= 1
    while i >= 0:
        result[k] = nums1[i]
        i -= 1
        k -= 1
    while j >= 0:
        result[k] = nums2[j]
        j -= 1
        k -= 1
    return result
        


def main():
    tests = [
        ([1, 3, 4, 6], [2, 5, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
    ]
    for nums1, nums2, result in tests:
        #assert result == merge(nums1, nums2)
        print(merge(nums1, nums2))


if __name__ == '__main__':
    main()
