# -*- coding: utf-8 -*-
"""
Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

"""
去重后，数量大于n/2
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in set(nums):
            if nums.count(i)>len(nums)/2:
                return i