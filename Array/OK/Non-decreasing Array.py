# -*- coding: utf-8 -*-
"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first
4
 to
1
 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""


"""
大于等于2说明两处以上导数为负值；
中间的需要保证特殊条件(画图)

"""
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        length = len(nums)
        if length<=2:
            return True
        for i in range(1,length):
            if nums[i]<nums[i-1]:
                count += 1
                if count == 2:
                    return False
                if (i != 1 and i != len(nums) - 1):
                    if (nums[i - 1] > nums[i + 1] and nums[i] < nums[i - 2]):
                        return False
        return True



A = Solution()
print A.checkPossibility([4,2,3])
