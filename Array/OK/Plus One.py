# -*- coding: utf-8 -*-
"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""
"""
数字和字符串转换
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        length = len(digits)
        sum = 0
        for i in range(length):
            sum+=digits[i]*pow(10,length-i-1)
        sum+=1
        array = list(str(sum))
        for i in range(len(array)):
            array[i]=int(array[i])
        return array

A = Solution()
print A.plusOne([9,9])

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 1
        for i in xrange(2, n + 1):
            result *= i
        return result

