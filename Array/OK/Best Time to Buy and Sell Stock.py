# -*- coding: utf-8 -*-
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"""
"""
被减数在前，减数在后，差值最大
如果后面的比前一个元素小，就以后面这个元素做被减数
动态规划，局部最优解和全局最优解,递推式最重要
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        cha = 0
        all_cha = 0
        for i in range(1,length):
            cha = max(cha+prices[i]-prices[i-1],0)
            all_cha = max(all_cha,cha)
        return all_cha