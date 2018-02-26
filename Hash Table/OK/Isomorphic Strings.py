"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        hs = {}
        ht = {}
        for j,i in enumerate(s):
            if i in hs:
                hs[i].append(j)
            else:
                hs[i] = [j]
        for j,i in enumerate(t):
            if i in ht:
                ht[i].append(j)
            else:
                ht[i] = [j]

        for v in hs.values():
            if v not in ht.values():
                return False
        return True
