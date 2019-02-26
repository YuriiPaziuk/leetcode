from selection import selection_sort
from insertion import insertion_sort
from shell import shell_sort
from merge import merge_sort
from quick import quick_sort



def main():
    tests = [
        [],
        [11],
        [11, 22],
        [22, 11],
        [11, 22, 33],
        [22, 33, 11]
    ]
    for nums in tests:
        #selection_sort(nums)
        #insertion_sort(nums)
        #shell_sort(nums)
        #merge_sort(nums)
        quick_sort(nums)
        print(nums)


if __name__ == '__main__':
    main()