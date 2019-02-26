# https://leetcode.com/problems/student-attendance-record-i/description/


def checkRecord(s):
    nA, nL = 0, 0
    for c in s:
        if c == 'P':
            nL = 0
        elif c == 'L':
            nL += 1
            if nL > 2: return False
        else: # c == 'A'
            nA += 1
            nL = 0
            if nA > 1: return False
    return True


def main():
    tests = [
        ('PPALLP', True),
        ('PPALLL', False)
    ]
    for s, result in tests:
        assert result == checkRecord(s), s


if __name__ == '__main__':
    main()
