# -*- coding: utf-8 -*-
"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Related problem: Reverse Words in a String II

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.
"""
"""
取余数，重新组合,nums=会重新开辟内存，num[:]=会修改nums
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        newk = k % n
        if newk != 0:
            """
            array1 = nums[0:n-newk]
            array2 = nums[n-newk:]
            for i in range(newk,n):
                nums[i]=array1[i-newk]
            for j in range(0,newk):
                nums[j]=array2[j]
            """
            nums[:] = nums[n-newk:]+nums[0:n-newk]


"""
>>>nums = [1,2,3]
>>>id(nums)
44393352L
>>>b = nums
>>>id(b)
44393352L
>>>a = nums[:]
>>>id(a)
44393160L
>>>nums[:]=[4,5,6]
>>>nums
[4, 5, 6]
>>>id(nums)
44393352L
>>>nums=[7,8,9]
>>>id(nums)
45311176L




"""