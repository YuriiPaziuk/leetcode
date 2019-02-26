def merge_sort(nums):

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    def sort(nums):
        if len(nums) < 2:
            return nums
        m = len(nums) // 2
        return merge(sort(nums[:m]), sort(nums[m:]))

    if len(nums) < 2:
        return
    else:
        result = sort(nums)
        nums.clear()
        nums.extend(result)