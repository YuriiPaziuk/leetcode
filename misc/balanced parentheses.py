"""
You are given an expression with numbers, brackets and operators.
For this task only the brackets matter. Brackets come in three flavors:
"{}" "()" or "[]". Brackets are used to determine scope or to restrict
some expression. If a bracket is open, then it must be closed with a
closing bracket of the same type. The scope of a bracket must not
intersected by another bracket. In this task you should make a decision,
whether to correct an expression or not based on the brackets. Do not
worry about operators and operands.

Input: An expression with different of types brackets as a string (unicode).

Output: A verdict on the correctness of the expression in boolean (True or False).

Precondition:
There are only brackets ("{}" "()" or "[]"), digits or operators ("+" "-" "*" "/").
"""
def brackets_ok(expression):
    brackets_open = '({['
    brackets_close = ')}]'
    matching_bracket = {br_close: br_open for br_open, br_close in zip(brackets_open, brackets_close)}
    stack = list()
    for symbol in expression:
        if symbol in brackets_open:
            stack.append(symbol)
        elif symbol in brackets_close:
            if not stack:
                return False
            if stack.pop() != matching_bracket[symbol]:
                return False
    return True if not stack else False


def main():
    tests = [
        ('', True),
        ('()', True),
        (')(', False),
        ('(', False),
        (')', False),
        ('(())', True),
        ('()()', True),
        ('(()', False),
        ('())', False),
        ('(()())', True),
        ('(()(()))', True),
        ("((5+3)*2+1)", True),
        ("{[(3+1)+2]+}", True),
        ("(3+{1-1)}", False),
        ("[1+1]+(2*2)-{3/3}", True),
        ("(({[(((1)-2)+3)-3]/3}-3)", False)
    ]
    for expression, result in tests:
        if result != brackets_ok(expression):
            print(expression, result, brackets_ok(expression))


if __name__ == '__main__':
    main()