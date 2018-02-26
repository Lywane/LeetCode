# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nex = []
        if not head or not head.next:
            return head

        while head.next:
            nex.append(head)
            head = head.next
        nex.append(head)
        for i in range(len(nex)-1,0,-1):
            nex[i].next = nex[i-1]
        nex[0].next = None
        head = nex[-1]
        return head


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        return prev