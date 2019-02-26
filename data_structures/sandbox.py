"""grades = [33, 55,45,87,88,95,34,76,87,56,45,98,87,89,45,67,45,67,76,73,33,87,12,100,77,89,92]
print(sum(grade > sum(grades)/len(grades) for grade in grades))

# a perfect number is equal to the sum of its divisors

def is_perfect(n):
    return n == sum(t for t in range(1, n) if n % t == 0)

for i in range(1, 1000):
    if is_perfect(i): print(i)


def collatz(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        n = n // 2 if n % 2 == 0 else n * 3 + 1
    sequence.append(1)
    return sequence

print(collatz(1000))
"""
def nonDivisibleSubset(k, arr):
    counts = [0] * k
    for num in arr:
        counts[num % k] += 1

    count = 0

    for i in range(k // 2 + 1):
        opposite = (k - i) % k
        if i == opposite:
            count += min(counts[i], 1)
        else:
            count += max(counts[i], counts[opposite])

    return count


print(nonDivisibleSubset(3, [1, 7, 2, 4]))
