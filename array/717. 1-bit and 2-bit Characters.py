"""
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input:
bits = [1, 0, 0]
Output: True
Explanation:
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input:
bits = [1, 1, 1, 0]
Output: False
Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
"""
class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i, n = 0, len(bits)
        while i < n - 1:
            i += 1 if bits[i] == 0 else 2
        return i == n - 1


def main():
    tests = [
        ([1, 0, 0], True),
        ([1, 1, 1, 0], False)
    ]
    for nums, result in tests:
        print(nums, result, Solution().isOneBitCharacter(nums))


if __name__ == '__main__':
    main()