"""
Given a singly linked list, determine if it is a palindrome.
"""




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        b = []
        flag = True
        while head:
            b.append(head.val)
            head = head.next

        for i in range(len(b) / 2):
            if b[i] != b[len(b) - i - 1]:
                flag = False
                break

        return flag