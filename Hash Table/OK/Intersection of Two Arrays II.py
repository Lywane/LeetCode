# -*- coding: utf-8 -*-
"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk,
and the memory is limited such that you cannot load all elements into the memory at once?
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """     
        #形成一个字典{元素：次数}，效率比先去重复再遍历获得次数强100倍，比直接遍历强1000倍
                hs = {}
                for n in nums1:
                    if n in hs:
                        hs[n] += 1
                    else:
                        hs[n] = 1

                ret = []
                for n in nums2:
                    if n in hs and hs[n] > 0:
                        hs[n] -= 1
                        ret.append(n)

                return ret
                """
        array=[]
        sett = set(nums1)&set(nums1)
        for i in sett:
            for j in range(min(nums1.count(i),nums2.count(i))):
                array.append(i)
        return array


