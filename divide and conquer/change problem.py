import functools


def change(coin_values, sum):
    """Return coins for sum"""
    result = dict()
    while sum > 0:
        if sum >= coin_values[0]:
            result[coin_values[0]] = result.get(coin_values[0], 0) + 1
            sum -= coin_values[0]
        else:
            coin_values = coin_values[1:]
    return result


@functools.lru_cache(maxsize=128)
def change_rec(coin_values, sum):
    """Return minimum number of coins for sum"""
    if sum == 0:
        return 0
    minnumcoins = 1000
    for coin in coin_values:
        if sum >= coin:
            numcoins = change_rec(coin_values, sum - coin)
            if numcoins + 1 < minnumcoins:
                minnumcoins = numcoins + 1
    return minnumcoins


@functools.lru_cache(maxsize=128)
def change(coin_values, sum):
    """Return coins for sum"""
    if sum == 0:
        return []
    if sum in coin_values:
        return [sum]
    result = []
    for coin in coin_values:
        if sum > coin:
            local_result = [coin] + change(coin_values, sum - coin)
            if not result or len(result) > len(local_result):
                result = local_result
    return result


def main():
    coin_values_ukr = [50, 25, 10, 5, 2, 1]
    coin_values_euro = [50, 20, 10, 5, 2, 1]
    coin_values_usa = [25, 10, 5, 1]
    coins = {
        'ukr': coin_values_ukr,
        'euro': coin_values_euro,
        'usa': coin_values_usa
    }
    #for country, coin_values in coins.items():
    #    print(country, change_rec(tuple(coin_values), 55))
    a = change(tuple([25, 20, 10, 5, 2, 1]), 40)
    print(a)

if __name__ == '__main__':
    main()