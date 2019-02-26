# https://leetcode.com/problems/roman-to-integer/description/


def romanToInt(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    current = previous = 0
    result = 0
    for c in s[::-1]:
        current = roman[c]
        if current < previous:
            result -= current
        else:
            result += current
        previous = current
    return result


def main():
    tests = [
        ('', 0),
        ('I', 1),
        ('V', 5),
        ('X', 10),
        ('VI', 6),
        ('LXXVI', 76),
        ('CDXCIX', 499),
        ('MMMDCCCLXXXVIII', 3888)
    ]
    for s, result in tests:
        #print(romanToInt(s))
        assert result == romanToInt(s), s
    print('Congrats!')


if __name__ == '__main__':
    main()
