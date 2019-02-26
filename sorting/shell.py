def shell_sort(nums):
    # https://oeis.org/A102549
    A102549 = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
    A102549.reverse()
    #for gap in A102549:
    for gap in gaps_fibo(len(nums)):
        for i in range(gap, len(nums), gap):
            j = i
            while j > 0 and j >= gap and nums[j - gap] > nums[j]:
                nums[j - gap], nums[j] = nums[j], nums[j - gap]
                j -= gap


def gaps(n):
    result = []
    k = 1
    step = (3 ** k - 1) // 2
    while step <= n // 3:
        result.append(step)
        k += 1
        step = (3 ** k - 1) // 2
    result.reverse()
    return result


def gaps_fibo(n):
    result = [1, 5, 8]
    while result[-1] < n // 3:
        result.append(result[-1] + result[-2])
    result.reverse()
    return result