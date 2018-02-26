"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process until the number
equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        array = list(str(n))
        all_sum = 0
        count = 0
        while count<10:
            for i in array:
                all_sum+=int(i)*int(i)
                count+=1
            if all_sum==1:
                return True
            array = list(str(all_sum))
            all_sum = 0
        return False

    """
    def isHappy(self, n):
        isValid = {}
        while (not n in isValid):
            isValid[n] = 1
            sqrt_sum = 0
            while (n > 0):
                curr_digit = n % 10
                sqrt_sum += curr_digit * curr_digit
                n /= 10
            if sqrt_sum == 1:
                return True
            else:
                n = sqrt_sum
        return False
    """