"""
Can you morph one word into another by just changing one letter at a time?
seek -> bark
"""
def load_words(filename):
    words = []
    with open(filename) as file:
        for line in file:
            if len(line.strip()) > 0:
                words.append(line.strip().lower())
    return words


def distance1(s1, s2):
    assert len(s1) == len(s2)
    equal_chars = sum(a == b for a, b in zip(s1, s2))
    return equal_chars == len(s1) - 1


def build_tree(root, words, used_words):
    # Find children of the current node
    current_word, children = list(root.items())[0]
    for word in words:
        if len(current_word) == len(word):
            if distance1(word, current_word) and word not in used_words:
                children.append({word: []})
                used_words.add(word)
    # Repeat for every child
    for child in children:
        build_tree(child, words, used_words)


def print_tree(root, prefix='|  '):
    current_word, children = list(root.items())[0]
    print(prefix, current_word, sep='')
    for child in children:
        print_tree(child, prefix + '|  ')


def find(root, word):
    current_word, children = list(root.items())[0]
    if current_word == word:
        return [word]
    for child in children:
        result = find(child, word)
        if result:
            return [current_word] + result
    return []


def main():
    words = load_words('linuxwords.txt')
    #words = ['abc', 'def', 'abd', 'dbc', 'dec']
    #for s1, s2 in zip(words[:-1], words[1:]):
    #    print(s1, s2, distance1(s1, s2))
    """root = {words[0]: []}
    used_words = set(words[0])
    used_words.add(words[0])"""
    start_word = 'absent'
    words = [word for word in words if len(word) == len(start_word)]
    root = {start_word: []}
    used_words = set()
    used_words.add(start_word)
    build_tree(root, words, used_words)
    print_tree(root)
    print(find(root, 'ascend'))


if __name__ == '__main__':
    main()
