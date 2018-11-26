# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curnode = head
        s = []
        while curnode:
            s.append(id(curnode))
            curnode = curnode.next
        t = s[-n]
        if id(head) == t:
            head = head.next
        else:
            d_curnode = head
            while d_curnode:
                if id(d_curnode.next) == t:
                    d = d_curnode.next
                    d_curnode.next = d.next
                    del d
                    break
                d_curnode = d_curnode.next
        return head
