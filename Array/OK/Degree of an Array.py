# -*- coding: utf-8 -*-
"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""

"""
先去重复，重复次数最大的元素的第一个位置到最后一个位置为subarray,长度为degree
找到重复次数最大的元素,获得的最小值
"""

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setnums = set(nums)
        degree = 0
        max_nums = []
        for i in setnums:
            if degree < nums.count(i):
                degree = nums.count(i)
                max_nums=[i]
            elif degree == nums.count(i):
                max_nums.append(i)
            else:
                pass
        if degree == 1:
            return 1

        length = 50,001
        all = len(nums)
        smun = nums[::-1]
        for j in max_nums:
            if all - smun.index(j)-nums.index(j) < length:
                length = all - smun.index(j)-nums.index(j)
        return length