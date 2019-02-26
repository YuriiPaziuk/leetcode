def fact_rec(n):
    return 1 if n == 1 else n * fact_rec(n-1)


def main():
    import math
    import random
    nof_tests = 10
    values_range = 1, 10
    for _ in range(nof_tests):
        n = random.randrange(*values_range)
        try:
            f = fact_rec(n)
            if f != math.factorial(n):
                print('Not equal to math.factorial for n = ', n, f, math.factorial(n))
        except:
            print('Exception raised for n = ', n)


if __name__ == '__main__':
    #main()
    import timeit
    print(timeit.timeit('fact_rec(100)', globals=globals(), number=1))