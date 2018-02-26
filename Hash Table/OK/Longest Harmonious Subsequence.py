# -*- coding: utf-8 -*-
"""
We define a harmonious array is an array where the difference between its maximum value and its minimum
value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all
its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.

"""
"""
获得{元素:频率}
"""

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        hs = {}
        for n in nums:
            if n in hs:
                hs[n] += 1
            else:
                hs[n] = 1
        for i in hs:
            if i+1 in hs:
                longest = max(longest,hs[i]+hs[i+1])
        return longest