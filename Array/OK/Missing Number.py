# -*- coding: utf-8 -*-
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""

"""
最简单思路，前n项和公式 (1+n)n/2
然后去掉列表的和,就得到缺失的数字
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 not in nums:
            return 0
        if 1 not in nums:
            return 1
        else:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = 1
        nums.append(1)
        for i in nums:
            nums[abs(i) - 1] = -abs(nums[abs(i) - 1])

        for j in range(len(nums)):
            if nums[j] > 0:
                return j+1


class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        return (n * (n+1))/2 - sum(nums)


