# -*- coding: utf-8 -*-
"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array.
Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute
difference is k.
Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
"""



class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        set1 = set()
        set2 = set()
        count = 0
        nums.sort()
        if k != 0:
            for i in nums:
                if i not in set1 and i-k in set1:
                    count+=1
                set1.add(i)
        elif k == 0:
            for i in nums:
                if i not in set2 and i in set1:
                    count+=1
                    set2.add(i)
                set1.add(i)
        return count

"""
class Solution(object):
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        count = 0
        if k == 0:
            d = {}
            #计算重复元素有多少个
            for x in nums:
                if d.has_key(x) and d[x] == 0:
                    count += 1
                    d[x] = 1
                elif not d.has_key(x):
                    d[x] = 0
            return count

        else:
            ss = set(nums)
            for i in ss:
                if i + k in ss:
                    count += 1
        return count


class Solution(object):
    def findPairs(self, nums, k):


        if k > 0:
            #去重后，每个元素加K，两个集合曲并集的长度
            return len(set(nums) & set(n + k for n in nums))
        elif k == 0:
            #获得出线次数大于1的元素总共多少个
            return sum(v > 1 for v in collections.Counter(nums).values())
        else:
            return 0
"""


A  =Solution()
print A.findPairs([3, 1, 4, 1, 5], k = 2)