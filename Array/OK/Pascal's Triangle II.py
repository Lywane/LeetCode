"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[int]
        """
        rowIndex = rowIndex+1
        array = []
        for i in range(1,rowIndex+1):
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
        return array[-1]