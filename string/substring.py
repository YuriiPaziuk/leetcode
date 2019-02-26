def read_file(filename):
    """Return a list with file lines"""
    result = []
    with open(filename) as file:
        for line in file:
            result.append(line.strip())
    return result


def find_pattern_naive(text, pattern):
    """Return a list with positions in text where pattern starts"""
    if not text or not pattern:
        return []
    result = []
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
        else:
            result.append(i)
    return result


def main():
    tests = [
        ('', '', []),
        ('a', 'a', [0]),
        ('abac', 'ab', [0]),
        ('abac', 'ba', [1]),
        ('abac', 'ac', [2]),
        ('abac', 'a', [0, 2]),
        ('abac', 'abac', [0]),
        ('aaa', 'a', [0, 1, 2])
    ]
    for text, pattern, result in tests:
        print(text, pattern, result, find_pattern_naive(text, pattern))

    ulisses = read_file('Ulysses_by_James_Joyce.txt')
    pattern = 'forward'
    result = []
    for line_number, line in enumerate(ulisses, 1):
        find_result = find_pattern_naive(line, pattern)
        if find_result:
            result.extend([(line_number, position + 1) for position in find_result])
    print(result)


if __name__ == '__main__':
    main()