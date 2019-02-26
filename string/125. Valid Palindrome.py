"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""
class Solution:
    def isPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0: return True
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def isPalindrome(self, s):
        t = [x for x in s.lower() if x.isalnum()]
        return t == t[::-1]


def main():
    with open('character_unit_palindromes.txt') as file:
        for line in file:
            assert Solution().isPalindrome(line.strip()) is True, line
    #print(Solution().isPalindrome('aba'))


if __name__ == '__main__':
    main()
