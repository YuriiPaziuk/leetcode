# https://leetcode.com/problems/detect-capital/description/


def detectCapitalUse(word):
    all_upper = lambda x: all(c.isupper() for c in x)
    all_lower = lambda x: all(c.islower() for c in  x)
    first_upper_then_lower = lambda x: x[0].isupper() and all_lower(x[1:])
    return all_upper(word) or all_lower(word) or first_upper_then_lower(word)


def main():
    tests = [
        ('USA', True),
        ('USa', False),
        ('uSa', False),
        ('usA', False),
        ('UsA', False),
        ('leetcode', True),
        ('Google', True)
    ]
    for word, result in tests:
        assert result == detectCapitalUse(word), (word, detectCapitalUse(word))


if __name__ == '__main__':
    main()
