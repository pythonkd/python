# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            slow = head
            fast = head.next
        else:
            return None
        while fast:
            # fast比slow多走了一圈
            # 在他们相遇的地点到环的最后一个节点之间的节点刚好等于从head到入环的第一个节点的前一个节点
            if fast == slow:
                slow_1 = head
                while True:
                    if slow_1 == slow.next:
                        return slow_1
                    else:
                        slow_1 = slow_1.next
                        slow = slow.next

            if fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return None
        return None

