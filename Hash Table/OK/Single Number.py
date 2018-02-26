# -*- coding: utf-8 -*-
"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""

"""
位运算 ^ 异或
因为A XOR A = 0，且XOR运算是可交换的，于是，对于实例{2,1,4,5,2,4,1}就会有这样的结果：

(2^1^4^5^2^4^1) => ((2^2)^(1^1)^(4^4)^(5)) => (0^0^0^5) => 5
就把只出现了一次的元素(其余元素均出现两次)给找出来了！

算法复杂度为O(n)，且不需要额外空间，代码如下：

class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for n in nums:
            result = result ^ n
        return result
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if not d.has_key(i):
                d[i]=0
                continue
            elif d.has_key(i) and d[i]==0:
                d[i]=1
        for i in d:
            if d[i]==0:
                return i