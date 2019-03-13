# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.reverse(root1, root2)

    def reverse(self, subtree1, subtree2):
        if subtree1 is None and subtree2 is None:
            return True
        elif subtree1 is None or subtree2 is None:
            return False
        else:
            if subtree1.val != subtree2.val:
                return False
            else:
                return (self.reverse(subtree1.left, subtree2.left) and self.reverse(subtree1.right,subtree2.right)) or \
                       (self.reverse(subtree1.right, subtree2.left) and self.reverse(subtree1.left,subtree2.right))