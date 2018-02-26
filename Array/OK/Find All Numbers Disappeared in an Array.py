# -*- coding: utf-8 -*-
"""
Given an array of integers where 1 <= a[i] <= n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

"""
"""
以元素为坐标，有这个元素，就把该坐标的元素变为负数，剩下没变负数的元素对应的坐标说明，没有这个元素
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array = []
        for i in nums:
            nums[abs(i)-1] = -abs(nums[abs(i)-1])
        for j in range(0,len(nums)):
            if nums[j] > 0:
                array.append(j+1)
        return array
