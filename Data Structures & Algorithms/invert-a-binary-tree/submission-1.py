# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        q = deque([root])
        
        while q:
            node = q.popleft()
            
            # 翻转当前节点的左右！！！
            node.left, node.right = node.right, node.left
            
            # 把孩子加入队列，继续翻转
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return root