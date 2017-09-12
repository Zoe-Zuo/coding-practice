# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True;
        else:
            return self.helper(root.left, root.right)
        
        
    def helper(self,L,R):
        if not L and not R:
            return True
        elif not L or not R:
            return False
        if L.val==R.val:
            outPair = self.helper(L.left, R.right)
            inPair = self.helper(L.right, R.left)
            return outPair and inPair
        else:
            return False
