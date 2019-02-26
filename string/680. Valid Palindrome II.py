"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                break
        if left >= right:
            return True
        s = s[left: right + 1]

        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]


def main():
    print(Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
    s = "ebcbbececabbacecbbcbe"
    print([(i, a) for i, a in enumerate(zip(s, reversed(s)))])


if __name__ == '__main__':
    main()
