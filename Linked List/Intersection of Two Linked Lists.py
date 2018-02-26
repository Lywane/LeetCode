"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 -- a2
                   -
                     c1 -- c2 -- c3
                   -
B:     b1 -- b2 -- b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        aa = []
        result = None
        st1 = headA
        st2 = headB
        while st1:
            aa.append(st1.val)
            st1.val = 10086789
            st1 = st1.next

        st1 = headA

        while st2:
            if st2.val == 10086789:
                result = st2
                break
            st2 = st2.next

        for i in range(len(aa)):
            st1.val = aa[i]
            st1 = st1.next
        return result


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        pointA = headA
        dic = {}
        while pointA:
            dic[pointA] = 1
            pointA = pointA.next

        pointB = headB

        while pointB:
            if pointB in dic:
                return pointB
            pointB = pointB.next

        return None
