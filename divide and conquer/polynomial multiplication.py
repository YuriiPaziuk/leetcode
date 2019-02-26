def mult_pol(a, b):
    n = max(len(a), len(b))
    result = [0] * (2 * n - 1)
    for i in range(n):
        for j in range(n):
            result[i + j] = result[i + j] + a[i] * b[j]
    return result


def main():
    n = 3
    a = [3, 2, 5]
    b = [5, 1, 2]
    # c = a * b
    c = [15, 13, 33, 9, 10]
    print(mult_pol(a, b))


if __name__ == '__main__':
    main()