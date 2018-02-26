# -*- coding: utf-8 -*-
"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
"""
类似递归
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        array = []
        for i in range(1,numRows+1):
            if i == 1:
                array.append([1])
            elif i == 2:
                array.append([1, 1])
            else:
                nums = [1]
                for j in range(1, i-1):
                    nums.append(array[i-2][j - 1] + array[i-2][j])
                nums.append(1)
                array.append(nums)
        return array