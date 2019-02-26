"""
Task: The goal of this code problem is to implement an algorithm for
the fractional knapsack problem.

Input Format: The first line of the input contains the number n of
items and the capacity W of a knapsack.

The next n lines define the values and weights of the items. The i-th
line contain integers v(i) and w(i) — the value and the weight of i-th
item, respectively.
Constraints: 1 ≤ n ≤ 10^3 , 0 ≤ W ≤ 2 · 10^6 ; 0 ≤ v(i) ≤ 2 · 106 ,
 0 < w(i) ≤ 2 · 10^6 for all 1 ≤ i ≤ n. All the numbers are integers.

Output Format: Output the maximal value of fractions of items that fit
into the knapsack. The absolute value of the difference between the answer
of your program and the optimal value should be at most 10 −3 . To ensure
this, output your answer with at least four digits after the decimal point
(otherwise your answer, while being computed correctly, can turn out to be
wrong because of rounding issues).
Time Limits: C: 1 sec, C++: 1 sec, Java: 1.5 sec, Python: 5 sec.
C#: 1.5 sec, Haskell: 2 sec, JavaScript: 3 sec, Ruby: 3 sec, Scala: 3 sec.
Memory Limit: 512 Mb

Sample 1
Input:
3 50
60 20
100 50
120 30
Output:
180.0000
Explanation:
To achieve the value 180, we take the first item and the third item into the bag.
"""
def values_to_take(knapsack_capacity, item_weights, item_values):
    """
    :param knapsack_capacity: int  7
    :param item_weights: list(int) [4, 3, 2]
    :param item_values: list(int)  [20, 18, 14]
    :return: list(int)             [2, 3, 2]
    """
    # Sort items in decreasing order by value per unit of weight
    items = sorted([(wi, vi, i) for i, (wi, vi) in enumerate(zip(item_weights, item_values))], key=lambda x: x[1]/x[0], reverse=True)
    result = []
    value_occupied = 0
    for wi, vi, i in items:
        # Take as much of the most valuable item as possible
        result.append(0)
        while wi > 0:
            if value_occupied < knapsack_capacity:
                value_occupied += 1
                result[-1] += 1
                wi -= 1
            else:
                break
        # Exit if knapsack is full
        if value_occupied == knapsack_capacity:
            break
    # Put the values into the initial order
    result = (sorted([(item[1], quantity, item[2]) for quantity, item in zip(result, items)], key=lambda x: x[2]))
    return [t[1] for t in result]


def total_value(values_taken, item_weights, item_values):
    return sum(value_taken / item_values * item_weight for value_taken, item_values, item_weight in zip(values_taken, item_weights, item_values))


def main():
    tests = [
        # knapsack_capacity, item_weights, item_values, vals_to_take, cost
        (7, [4, 3, 2], [20, 18, 14], [2, 3, 2], 42)
    ]
    for knapsack_capacity, item_weights, item_values, vals_to_take, cost in tests:
        print(values_to_take(knapsack_capacity, item_weights, item_values))
        print(total_value(values_to_take(knapsack_capacity, item_weights, item_values), item_weights, item_values))


if __name__ == '__main__':
    main()