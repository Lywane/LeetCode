"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None

        st = ListNode(10086)
        st.next = head
        count = 0
        tmp = None
        while st.next:
            if st.next.val == val:
                st.next = st.next.next
            else:
                if count == 0:
                    tmp = st.next
                count += 1
                st = st.next

        return tmp