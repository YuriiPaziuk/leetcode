"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""
class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        words_dict = {word: i for i, word in enumerate(words)}
        result = []

        for i, word in enumerate(words):
            for j in range(len(word) + 1):

                left, right = word[:j], word[j:]
                reversed_left, reversed_right = left[::-1], right[::-1]

                if j != 0 and left == reversed_left:
                    if reversed_right in words_dict and words_dict[reversed_right] != i:
                        result.append([words_dict[reversed_right], i])

                if right == reversed_right:
                    if reversed_left in words_dict and words_dict[reversed_left] != i:
                        result.append([i, words_dict[reversed_left]])

        return result


def main():
    tests = [
        (["bat", "tab", "cat"], [[0, 1], [1, 0]]),
        (["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [3, 2], [2, 4]])
    ]
    for words, result in tests:
        print(result, Solution().palindromePairs(words))


if __name__ == '__main__':
    main()
