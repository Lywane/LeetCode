# -*- coding: utf-8 -*-
"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
"""
判断t是不是由s的几个字母反转得到的，统计次数即可
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==len(t):
            for i in set(s):
                if list(s).count(i)!=list(s).count(i):
                    return False
            return True
        return False