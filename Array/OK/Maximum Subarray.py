# -*- coding: utf-8 -*-
"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

"""
"""
返回和最大的子串的和
如果子串加上元素，没有元素本身大，那么子串改为这个元素
动态规划
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_sums = nums[0]
        sums = nums[0]
        length = len(nums)
        for i in range(1,length):
            sums = max(nums[i]+sums,nums[i])
            all_sums = max(sums,all_sums)
        return all_sums


