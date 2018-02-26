# -*- coding: utf-8 -*-
"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]
Output: 4

Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
"""

"""
最大的永远加不到，为了让拥有最大数的那组最大，用倒数第二个和他匹配，然后依次往前推。
"""
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0
        for i in range(len(nums)):
            if i % 2 ==0:
                sum+=nums[i]
        return sum