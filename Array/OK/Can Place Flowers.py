# -*- coding: utf-8 -*-
"""
Suppose you have a long flowerbed in which some of the plots are planted and some are not.
However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n,
return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""

"""
一朵不中肯定可以
只有一个地方就只判断自身
边缘单独判断
中间判断两边,每次中植一棵，该位置状态改变
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        count = 0
        length = len(flowerbed)
        if length == 1:
            if flowerbed[0]==0:
                if n > 1:
                    return False
                else:
                    return True
            else:
                return False

        for i in range(length):
            if flowerbed[i]==0:
                if i == 0 and flowerbed[1] == 0:
                    count+=1
                    flowerbed[i]=1
                elif i == length-1 and flowerbed[length-2] == 0:
                    count+=1
                    flowerbed[i] = 1
                elif 0<i<length-1 and flowerbed[i-1] ==0 and flowerbed[i+1] == 0:
                    count+=1
                    flowerbed[i] = 1
        return count>=n
