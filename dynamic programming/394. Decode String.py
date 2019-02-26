"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''
        if s[0].isdigit():
            num = s[:self.n(s)]
            start, stop = self.n(s), self.matching(s, self.n(s))
            return int(num) * self.decodeString(s[start+1:stop-1]) + self.decodeString(s[stop:])
        else:
            return s[0] + self.decodeString(s[1:])

    def matching(self, s, i):
        count, j = 1, i + 1
        while count > 0:
            if s[j] == '[':
                count += 1
            elif s[j] == ']':
                count -= 1
            j += 1
        return j

    def n(self, s):
        for i in range(len(s)):
            if s[i] == '[':
                return i


def main():
    tests = [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("11[a]", "aaaaaaaaaaa")
    ]
    for s, result in tests:
        print(s, result, Solution().decodeString(s))
        #print(s, result, Solution().matching(s, 1))


if __name__ == '__main__':
    main()