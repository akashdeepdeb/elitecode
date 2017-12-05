# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        prv = None
        nex = head.next
        cur = head
        while cur != None:
            cur.next = prv
            prv = cur
            cur = nex
            if nex is not None:
                nex = nex.next
        return prv
