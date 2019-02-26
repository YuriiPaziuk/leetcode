"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""
class Solution:

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) == 0 and len(p) == 0:
            return True
        if len(s) == 0 and p == '*':
            return True
        if len(s) == 0 or len(p) == 0:
            return False
        if p[0] != '?' and p[0] != '*':
            return False if s[0] != p[0] else self.isMatch(s[1:], p[1:])
        if p[0] == '?':
            return self.isMatch(s[1:], p[1:])
        if p[0] == '*':
            if len(p) == 1:
                return True
            if p[1] == '*' or p[1] == '?':
                return self.isMatch(s, p[1:])
            if ('?' not in p) and ('*' not in p[1:]):
                return s.endswith(p[1:])
            while s and s[0] != p[1]:
                s = s[1:]
            return False if not s else self.isMatch(s, p[1:])


def main():
    # tests = (string, pattern, result)
    tests = [
        ('', '', True),
        ('a', 'a', True),
        ('aa', 'a', False),
        ('aa', 'ab', False),
        ('aa', 'aa', True),
        ('aaa', 'aa', False),
        ('a', '?', True),
        ('ab', '??', True),
        ('ab', '?a', False),
        ('ab', '?b', True),
        ('ab', 'a?', True),
        ('aa', 'a*', True),
        ('aa', '*', True),
        ('aa', '*a', True),
        ('aba', '*a', True),
        ('abcdefg', 'a*de*g', True),
        ('abcadeafaga', 'a*adea*a', True),
        ('abcdefg', '?bc*f?', True),
        ("abefcdgiescdfimde", "ab*cd?i*de", True),
        ("aaaa", "***a", True),
        ("", "*", True),
        ('a', '*?*', True)
    ]
    for test in tests:
        if Solution().isMatch(test[0], test[1]) != test[2]:
            print(test[0], test[1], Solution().isMatch(test[0], test[1]), test[2])


if __name__ == '__main__':
    main()