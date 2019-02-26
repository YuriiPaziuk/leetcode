"""
You have a job interview. Instead of negotiating your salary,
they give you a few pieces of paper with digits written on them.
Your task is to arrange these digits in a row, so when you read
the number from left to right, that will be your salary. It is
pretty obvious that you should arrange you numbers from largest
to the smallest from left to right.

Algorithm.
1. Find max digit.
2. Append it to the number.
3. Remove it from the list.
4. Go to step 1 if there are still numbers in the initial list.
"""
def max_salary_greedy_int(nums):
    """
    Return max number, that can be formed from given nums. Greedy
    approach: while there are numbers left, take the biggest one.

    Numbers are compared to each other as ints.

    :param nums: list(int)
    :return: int
    """
    nums_copy = nums.copy()
    result = []
    while nums_copy:
        max_number = max(nums_copy)
        result.append(max_number)
        nums_copy.remove(max_number)
    return int(''.join([str(num) for num in result]))


def max_salary_greedy_str(nums):
    """
    Return max number, that can be formed from given nums. Greedy
    approach: while there are numbers left, take the biggest one.

    Numbers are compared to each other as str.

    :param nums:list(int)
    :return: int
    """
    str_nums = [str(num) for num in nums]
    return int(''.join(sorted(str_nums, reverse=True)))


def max_salary_brute_force(nums):
    import itertools
    str_nums = [str(num) for num in nums]
    best = int("".join(str_nums))
    for permutation in itertools.permutations(str_nums):
        current = int("".join(permutation))
        if current > best:
            best = current
    return best


def max_salary_good(nums):
    class Compare(str):
        def __lt__(self, other):
            return self+other > other+self

    result = ''.join(sorted(map(str, nums), key=Compare))
    return '0' if result[0] == '0' else result


def max_salary_good2(nums):
    from functools import cmp_to_key

    def cmp(x, y):
        a, b = x + y, y + x
        if   a > b:  return  1
        elif a == b: return  0
        else:        return -1

    nums = [str(x) for x in nums]
    nums.sort(key=cmp_to_key(cmp), reverse=True)
    return ''.join(nums).lstrip('0') or '0'

def stress_test():
    import random
    nof_tests = 100
    nums_size = 1, 4  # min max
    nums_values = 1, 100  # min max
    for _ in range(nof_tests):
        current_size = random.randrange(*nums_size)
        nums = [random.randrange(*nums_values) for _ in range(current_size)]
        greedy_int = max_salary_greedy_int(nums)
        greedy_str = max_salary_greedy_str(nums)
        brute_force = max_salary_brute_force(nums)
        good = max_salary_good(nums)
        #if not greedy_int == greedy_str == brute_force == good:
        if not brute_force == int(good):
            print(nums, brute_force, good)
            #print(nums, greedy_int, greedy_str, brute_force, good)


def main():
    tests = [
        ([9,5,9,3,7,1], 997531),
        ([12, 9], 912),
        ([3, 30, 34, 5, 9], 9534330)
    ]

    for nums, result in tests:
        print(nums, '\t', result, '\t',
              max_salary_greedy_int(nums), '\t',
              max_salary_greedy_str(nums), '\t',
              max_salary_brute_force(nums), '\t',
              max_salary_good2(nums))


if __name__ == '__main__':
    main()
    #stress_test()
