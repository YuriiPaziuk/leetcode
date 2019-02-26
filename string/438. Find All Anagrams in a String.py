"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
class Solution:
    def findAnagrams1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        import collections

        len_s, len_p = len(s), len(p)
        pattern = collections.Counter(p)
        sliding_window = collections.Counter(s[:len_p - 1])
        result = []

        i = 0
        while i + len_p <= len_s:
            sliding_window[s[i + len_p - 1]] += 1
            if pattern == sliding_window:
                result.append(i)
            sliding_window[s[i]] -= 1
            if sliding_window[s[i]] == 0:
                del sliding_window[s[i]]
            i += 1

        return result

    def findAnagrams(self, s, p):

        if len(s) == 0: return []
        if len(s) < len(p): return []

        char_to_int = lambda x: ord(x) - 97
        len_s, len_p = len(s), len(p)
        p_counts, window = [0] * 26, [0] * 26
        result = []

        s_ords = list(map(char_to_int, s))

        for i in map(char_to_int, p):
            p_counts[i] += 1

        for i in range(len_p):
            window[s_ords[i]] += 1

        if p_counts == window:
            result.append(0)

        for i in range(len_p, len_s):
            window[s_ords[i]] += 1
            window[s_ords[i - len_p]] -= 1
            if p_counts == window:
                result.append(i - len_p + 1)

        return result


def main():
    tests = [
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2])
    ]
    for s, p, result in tests[:]:
        #Solution().findAnagrams(s, p)
        print(result, Solution().findAnagrams(s, p))


if __name__ == '__main__':
    main()
