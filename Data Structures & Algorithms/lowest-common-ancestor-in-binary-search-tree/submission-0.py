# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        while root:
            # 都比当前小 → 去左
            if p.val < root.val and q.val < root.val:
                root = root.left
            
            # 都比当前大 → 去右
            elif p.val > root.val and q.val > root.val:
                root = root.right
            
            # 一个左一个右 / 一个是自己 → 就是答案
            else:
                return root