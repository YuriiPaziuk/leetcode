"""
mplement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        _trie = lambda: collections.defaultdict(_trie)
        self.trie = _trie()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.trie
        for letter in word:
            current = current[letter]
        current['KEYWORD'] = word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.trie
        for letter in word:
            if letter not in current: break
            current = current[letter]
        return 'KEYWORD' in current and current['KEYWORD'] == word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.trie
        for letter in prefix:
            if letter not in current: return False
            current = current[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


def main():
    seashells = 'she sells seashells on a sea shore'
    seashells += ' the shells she sells are surely seashells'
    trie = Trie()

    words = 'hello hell helloa hello hell helloa hello'
    words = words.split()

    trie.insert('hello')
    print(trie.search('hell'))
    print(trie.search('helloa'))
    print(trie.search('hello'))

    print(trie.startsWith('hell'))
    print(trie.startsWith('helloa'))
    print(trie.startsWith('hello'))
    """
    print(trie.search('a'))
    print(trie.startsWith('a'))

    for word in seashells.split():
        trie.insert(word)

    print(trie.search('b'))
    print(trie.startsWith('b'))
    """

if __name__ == '__main__':
    main()
