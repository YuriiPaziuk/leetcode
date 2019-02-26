"""
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:
Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Note:
The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000
"""
class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        # 182 ms
        import collections
        Tree = lambda: collections.defaultdict(Tree)
        self.trie = Tree()

        def add_word_to_trie(word):
            current = self.trie
            for letter in word:
                current = current[letter]
            current['KEYWORD'] = word

        def replace(word):
            current_node = self.trie
            for letter in word:
                if letter not in current_node: break
                current_node = current_node[letter]
                if 'KEYWORD' in current_node:
                    return current_node['KEYWORD']
            return word

        for word in dict:
            add_word_to_trie(word)

        return ' '.join(map(replace, sentence.split()))

    def replaceWords2(self, dict, sentence):
        # 292 ms
        dict = set(dict)

        def replace(word):
            for i in range(1, len(word) + 1):
                if word[:i] in dict:
                    return word[:i]
            return word

        return ' '.join(map(replace, sentence.split()))


def main():
    seashells = 'she sells seashells on a sea shore'
    seashells += ' the shells she sells are surely seashells'
    print(Solution().replaceWords2(seashells.split(), seashells))


if __name__ == '__main__':
    main()
