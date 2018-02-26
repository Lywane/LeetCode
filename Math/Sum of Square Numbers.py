"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
"""
from math import sqrt
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l = 0
        r = int(sqrt(c))
        while l <= r:
            if l*l + r*r == c:
                return True
            elif l*l + r*r < c:
                l+=1
                continue
            elif l*l + r*r > c:
                r-=1
                continue
        return False

A = Solution()
print A.judgeSquareSum(68)