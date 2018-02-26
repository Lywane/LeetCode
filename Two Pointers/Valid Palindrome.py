"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower().strip()
        i = 0
        j = len(s)-1
        while i<j:
            if s[i].isalpha() or s[i].isdigit():
                if s[j].isalpha() or s[j].isdigit():
                    if s[j]!=s[i]:
                        return False
                    else:
                        i+=1
                        j-=1
                else:
                    j-=1
            else:
                i+=1
        return True