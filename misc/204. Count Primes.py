"""
Description:

Count the number of prime numbers less than a non-negative number, n.
"""
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i + i: n: i] = [False] * len(primes[i + i: n: i])
        return sum(primes)

    def countPrimes2(self, n):
        if n < 3: return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i + i, n, i):
                    primes[j] = False
        return sum(primes)


def main():
    for n in range(1, 50):
        print(n, Solution().countPrimes(n), Solution().countPrimes2(n))
        #print(n, Solution().countPrimes2(n))


if __name__ == '__main__':
    main()
