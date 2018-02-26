# -*- coding: utf-8 -*-
"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number.
The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

"""
"""
获得最大三个数
"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array = set(nums)
        mx1 = None
        mx2 = None
        mx3 = None
        for i in array:
            if i > mx3:
                mx3 = mx2
                if i > mx2:
                    mx2 = mx1
                    if i > mx1:
                        mx1 = i
                    else:
                        mx2 = i
                else:
                    mx3 = i
        if mx3 != None:
            return mx3
        else:
            return mx1