"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        org = 1
        while n/pow(5,org)>=1:
            a+=n/pow(5,org)
            org+=1
        return a

A = Solution()
print A.trailingZeroes(110)


