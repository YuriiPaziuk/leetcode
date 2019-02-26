# https://leetcode.com/problems/unique-morse-code-words/description/


class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        pass


def main():
    from string import ascii_lowercase
    codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    morze = dict(zip(ascii_lowercase, codes))
    t = ''.join(morze[t] for t in 'gin')
    print(t)
    words = ["gin", "zen", "gig", "msg"]
    print(len(set(''.join(morze[t] for t in word) for word in words)))


if __name__ == '__main__':
    main()
