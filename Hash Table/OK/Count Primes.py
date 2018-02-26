"""
Description:

Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

"""
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        listVal = [True] * n
        print listVal
        listVal[0] = listVal[1] = False
        for i in range(2,n):
            if listVal[i] == True:
                if i*i > n:
                    break
                for j in range(i+1,n):
                    if j % i == 0:
                        listVal[j] = False
        return listVal.count(True)


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        prime = [True] * n
        prime[:2] = [False, False]
        for base in xrange(2, int((n - 1) ** 0.5) + 1):
            if prime[base]:
                prime[base ** 2::base] = [False] * len(prime[base ** 2::base])
        return sum(prime)

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        import numpy as np
        primes = np.ones(n/2, dtype=np.bool)
        for i in range(3, int(n**0.5)+1, 2):
            if primes[i/2]:
                primes[i*i/2::i] = False
        return int(primes.sum())

A = Solution()
print A.countPrimes(10000)