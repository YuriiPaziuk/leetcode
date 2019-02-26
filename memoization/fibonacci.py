import functools
import timeit


def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = func(*args)
        return result

    return memoized_func


#@memoize
@functools.lru_cache(maxsize=128)
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def main():
    print(timeit.timeit('fibo(35)', globals=globals(), number=1))


if __name__ == '__main__':
    main()