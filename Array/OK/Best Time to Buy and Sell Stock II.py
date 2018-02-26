# -*- coding: utf-8 -*-
"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
"""
只要后一天比前一天贵，就可以赚钱
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        all = 0
        for i in range(1,length):
            new = prices[i]
            old = prices[i - 1]
            if new > old:
                all +=new - old
        return all