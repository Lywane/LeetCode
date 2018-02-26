"""Determine whether an integer is a palindrome. Do this without extra space."""
class Solution(object):
    def isPalindrome(self, n):
        """
        :type x: int
        :rtype: bool
        """
        n = str(n)
        m = n[::-1]
        return n == m