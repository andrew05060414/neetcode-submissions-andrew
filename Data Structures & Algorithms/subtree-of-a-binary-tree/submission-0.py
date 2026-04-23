# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:        
        # 如果大树空了，找不到
        if not root:
            return False
        
        # 如果当前节点刚好是相同的树 → True
        if self.isSameTree(root, subRoot):
            return True
        
        # 否则去左边找 OR 去右边找
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # 直接把你上一题的代码搬过来！
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)