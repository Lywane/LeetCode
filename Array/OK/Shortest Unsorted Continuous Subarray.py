# -*- coding: utf-8 -*-
"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order,
then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""
"""
找到需要重新排序的最短子串，重新排序让整个列表有序，返回该子串的长度
思路是排序后和原先列表对比，找到第一个不同的和最后一个不同的，返回坐标差值
"""

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        soo = sorted(nums)
        stt = 0
        end = -1
        for i in range(length):
            if nums[i]!=soo[i]:
                stt = i
                break
        for i in range(length-1,0,-1):
            if nums[i]!=soo[i]:
                end = i
                break
        return end-stt+1