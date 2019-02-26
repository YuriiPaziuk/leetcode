# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':

        if len(prices) < 2:
            return 0

        return buy



def main():
    tests = [
        ([7,1,5,3,6,4], 7),
        ([1,2,3,4,5], 4),
        ([7,6,4,3,1], 0),
        ([1, 2], 1),
        ([5, 3], 0)
    ]
    for input, output in tests:
        print(input, output, Solution().maxProfit(input))


if __name__ == '__main__':
    main()
