"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = []
        hs = ['a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U']
        ss = list(s)
        for i in xrange(len(ss)):
            if ss[i] in hs:
                temp.append(i)
        i = 0
        j = len(temp) - 1
        while i < j:
            ss[temp[i]], ss[temp[j]] = ss[temp[j]], ss[temp[i]]
            i += 1
            j -= 1
        return ''.join(ss)
