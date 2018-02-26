# -*- coding: utf-8 -*-
"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6

Example 2:
Input: [1,2,3,4]
Output: 24

Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""
"""
排序后返回最大三个数和最小两个与最大乘积之间大的一个:
三正数：最大三个
三负数：最大三个
2正数1负数：最大三个
2负数1正数：最小两个最大1个
其实不需要排序，获得需要的五个数就行了
"""

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-3]*nums[-2]*nums[-1],nums[0]*nums[1]*nums[-1])