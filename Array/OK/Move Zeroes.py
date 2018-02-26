# -*- coding: utf-8 -*-
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""

"""
是0就记录一个偏移量，不是0，就把元素和之前一堆0中的第一个0换位置
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = 0
        for i in range(length):
            if nums[i]==0:
                k+=1
            else:
                q = nums[i]
                nums[i] = 0
                nums[i-k]=q

        return nums
