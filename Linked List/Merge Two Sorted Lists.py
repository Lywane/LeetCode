"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 and not l2:
            head = l1
            return head
        elif l2 and not l1:
            head = l2
            return head
        elif not l1 and not l2:
            head = None
            return head
        elif l1.val <= l2.val:
            head = l1
            t1 = l1.next
            t2 = l2
        elif l1.val > l2.val:
            head = l2
            t1 = l1
            t2 = l2.next

        tmp = head
        while t1 and t2:
            if t1.val <= t2.val:
                tmp.next = t1
                tmp = tmp.next
                t1 = t1.next

            else:
                tmp.next = t2
                tmp = tmp.next
                t2 = t2.next

        if t1:
            tmp.next = t1
        elif t2:
            tmp.next = t2
        return head

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2: return
        result = ListNode(0)
        l = result
        while l1 and l2:
            if l1.val < l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            #融合后链表的下一位,当前位置刚刚赋值
            l = l.next
        #把剩余的链表排在后面
        l.next = l1 or l2
        #返回融合后链表从第二个对象开始，第一个对象是自己创建的ListNode(0)
        return result.next