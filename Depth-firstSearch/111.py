# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        L=self.minDepth(root.left)
        R=self.minDepth(root.right)
        if L==0 or R==0:
            h = 1+R if L==0 else 1+L
            return h
        else:
            return 1+min(L,R)