class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curnode = head
        while curnode:
            t = curnode.val
            n_curnode = curnode.next
            while hasattr(n_curnode, 'val') and n_curnode.val == t:
                n_curnode = n_curnode.next
                curnode.next = n_curnode
            curnode = curnode.next
        return head