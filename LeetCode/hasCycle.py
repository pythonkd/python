# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head and head.next :
            slow = head
            fast = head.next
        else:
            return False
        while fast:
            if slow == fast:
                return True
            if fast.next:
                fast = fast.next.next
                slow = slow.next
            else :
                return False
        return False