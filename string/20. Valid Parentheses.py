# https://leetcode.com/problems/valid-parentheses/description/

def isValid(s):
    t = []
    open_par = {'(', '[', '{'}
    close_par = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in open_par:
            t.append(c)
        else:
            if t and t[-1] == close_par[c]:
                t.pop()
            else:
                return False
    return len(t) == 0
        


def main():
    tests = [
        ('(){}[](())({[]})', True),
        ('((())', False),
        ('())', False)
    ]
    for s, result in tests:
        assert result == isValid(s), s


if __name__ == '__main__':
    main()
