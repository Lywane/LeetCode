"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

Credits:
Special thanks to @minglotus6 for adding this problem and creating all test cases.
"""
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern)==0 and len(str)!=0:
            return False
        p = list(pattern)
        s = str.split(' ')

        hs = {}
        ht = {}
        for j,i in enumerate(p):
            if i in hs:
                hs[i].append(j)
            else:
                hs[i] = [j]
        for j,i in enumerate(s):
            if i in ht:
                ht[i].append(j)
            else:
                ht[i] = [j]

        for v in hs.values():
            if v not in ht.values():
                return False
        return True
