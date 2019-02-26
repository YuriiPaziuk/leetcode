"""
Suppose you are a farmer with a plot of land. You want to divide
this farm evenly into square plots. You want the plots to be as big
as possible.
"""
def biggest_square(x, y):
    short, long = min(x, y), max(x, y)
    return short if long % short == 0 else biggest_square(long - short, short)


def main():
    tests = [
        (1, 1, 1),
        (1, 2, 1),
        (8, 12, 4),
        (10, 25, 5),
        (640, 1680, 80)
    ]
    for width, length, result in tests:
        print(width, length, result, biggest_square(width, length))


if __name__ == '__main__':
    main()