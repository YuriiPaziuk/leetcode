"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
"""
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        import collections
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return [anagrams[sorted_word] for sorted_word in anagrams]


def main():
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == '__main__':
    main()
