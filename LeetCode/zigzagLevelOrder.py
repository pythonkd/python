# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.s = list()
        self.queue = deque()
        self.layer_trav(root)
        for i, j in enumerate(self.s):
            if i % 2 != 0:
                j.reverse()
        return self.s

    def layer_trav(self, subtree):
        if subtree:
            self.queue.append(subtree)
            while self.queue:
                tmp = list()
                size = len(self.queue)
                while size > 0:
                    tree = self.queue.popleft()
                    tmp.append(tree.val)
                    if tree.left:
                        self.queue.append(tree.left)
                    if tree.right:
                        self.queue.append(tree.right)
                    size -= 1
                self.s.append(tmp)