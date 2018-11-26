# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        s = []
        for nodes in lists:
            while nodes:
                s.append(nodes.val)
                nodes = nodes.next
        s.sort()
        Node = ListNode(0)
        curnode = Node
        for i in s:
            node = ListNode(i)
            curnode.next = node
            curnode = curnode.next
        return Node.next