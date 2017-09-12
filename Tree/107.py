# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l = self.level(root)
        res = [None]*l
        self.helper(root, l, res)
        return res
        
    def helper(self, root, level, res):
        if not root:
            return
        self.helper(root.left,level-1,res)
        self.helper(root.right,level-1,res)
        if res[level-1]==None:
            a=[]
            a.append(root.val)
            res[level-1]=a
        else:
            res[level-1].append(root.val)
        return   
    
    def level(self, root):
        if not root:
            return 0
        L=self.level(root.left)
        R=self.level(root.right)
        return 1+max(L,R)
        