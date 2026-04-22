# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result = False
        if not p and not q:
            return True
        elif not p:
            return False
        elif not q:
            return False
        elif p.val != q.val:
            return False
        
        # val are same or both empty

        # campare left
        l = self.isSameTree(p.left,q.left)
        r = self.isSameTree(p.right,q.right)

        if l and r:
            return True
        else:
            return False