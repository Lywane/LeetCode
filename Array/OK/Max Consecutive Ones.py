# -*- coding: utf-8 -*-
"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

"""
是1就开始计数，是0就把计数给arrays，然后计数清零，请零前和现有arrays比较
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arrays = 0
        array = 0
        for i in nums:
            if i == 1:
                array += 1
            else:
                if arrays < array:
                    arrays = array
                array = 0
        if arrays < array:
            arrays = array
        return arrays
