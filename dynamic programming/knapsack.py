"""
Knapsack problem:
1. Fractional knapsack. Greedy algorithm.
2. Discreet knapsack.
    2.1. With repetitions (unlimited quantities).
    2.2. Without repetitions (one of each items).

Input:
wi - weights
vi - values
W - total weight

Output:
Maximum value of items whose weight doesn't exceed W.

items: (6, $30), (3, $14), (4, $16), (2, $9)
W = 10
Without repetitions: (6, $30) + (4, $16) = (10, $46)
With repetitions: (6, $30) + (2, $9) + (2, $9) = (10, $48)
Fractional: (6, $30) + (3, $14) + (1, $4.5) = (10, $48.5)
"""

def knapsack(items, W):
    """Without repetitions (one of each item)"""

    def items_value(items):
        return sum(item[1] for item in items)

    if W == 0 or not items:
        return []
    if len(items) == 1 and items[0][0] <= W:
        return items
    result = []
    for item in items:
        if W - item[0] >= 0:
            subitems = items.copy()
            subitems.remove(item)
            local_result = [item] + knapsack(subitems, W - item[0])
            if not result or items_value(result) < items_value(local_result):
                result = local_result
    return result


def k(items, W):
    """With repetitions (unlimited quantities)"""

    def items_value(items):
        return sum(item[1] for item in items)

    if W == 0 or not items:
        return []
    if len(items) == 1 and items[0][0] <= W:
        return items
    result = []
    for item in items:
        if W - item[0] >= 0:
            local_result = [item] + knapsack(items, W - item[0])
            if not result or items_value(result) < items_value(local_result):
                result = local_result
    return result


def main():
    w = [6, 3, 4, 2]  # weights
    v = [30, 14, 16, 9]  # values
    items = list((wi, vi) for wi, vi in zip(w, v))
    knapsack_value = 10
    print(k([(1, 2), (2, 3)], 2))
    print(k(items, knapsack_value))


if __name__ == '__main__':
    main()