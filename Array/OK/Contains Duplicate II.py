# -*- coding: utf-8 -*-
"""
Given an array of integers and an integer k, find out whether there are two distinct indices
i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""
"""
先判断是否有重复，没重复直接返回false；
然后判断是不是长度小于k+1,是的话直接返回true(必定重复)；
在将判断窗口不断右移，寻找符合条件
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(set(nums)) == len(nums):
            return False
        if len(nums)<=k+1:
            return True
        array = nums[:k+1]
        if len(set(array))!=k+1:
            return True
        for i in range(k+1,len(nums)):
            if len(set(nums[i-k:i+1]))!=k+1:
                return True
        return False
