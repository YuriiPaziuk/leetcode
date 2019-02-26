# https://leetcode.com/problems/repeated-string-match/description/


def repeatedStringMatch(A, B):
    '''from math import ceil
    t = ceil(len(B) / len(A))
    for i in range(2):
        if B in A * (t + i):
            return t + i
    return -1'''
    if B in A: return 1
    elif not set(B).issubset(set(A)): return -1

    t = -(-len(B) // len(A))
    
    s = A * t
    if B in s: return t
    
    s += A
    if B in s: return t + 1
    
    return -1


def main():
    tests = [
        ('abcd', 'cdabcdab', 3)
    ]
    for A, B, result in tests:
        assert result == repeatedStringMatch(A, B), repeatedStringMatch(A, B)


if __name__ == '__main__':
    main()
