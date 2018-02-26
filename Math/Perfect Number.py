"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
"""


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        org = num
        l=2
        r=num/2+1
        while l<r:
            if num % l == 0:
                org = org - l - num/l
            l+=1
            r = num / l
        if org==1:
            return True
        else:
            return False

A = Solution()
print A.checkPerfectNumber(28)


