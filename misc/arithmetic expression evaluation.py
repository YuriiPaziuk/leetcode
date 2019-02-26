def evaluate(expr):
    import math
    supported_operations = ['+', '-', '*', '/', 'sqrt']
    operations, operands = list(), list()
    for x in expr.split():
        if x in supported_operations:
            operations.append(x)
        elif x == '(':
            pass
        elif x == ')':
            operation = operations.pop()
            if operation == 'sqrt':
                operand = operands.pop()
                operands.append(math.sqrt(operand))
            else:
                operand2 = operands.pop()
                operand1 = operands.pop()
                if   operation == '+': result = operand1 + operand2
                elif operation == '-': result = operand1 - operand2
                elif operation == '*': result = operand1 * operand2
                elif operation == '/': result = operand1 / operand2
                operands.append(result)
        else:
            operands.append(float(x))
    return operands.pop()


def main():
    tests = [
        ('( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )', 101),
        ('( ( 1 + sqrt ( 5.0 ) ) / 2.0 )', 1.618033988749895),
        ('1', 1),
        ('( 1 + ( 2 * 3 ) )', 7),
        ('( ( 1 + 2 ) * 3 )', 9)
    ]
    for expression, result in tests[3:]:
        print(expression, result, evaluate(expression))


if __name__ == '__main__':
    main()