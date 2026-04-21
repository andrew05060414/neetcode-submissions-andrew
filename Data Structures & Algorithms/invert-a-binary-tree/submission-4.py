# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # 停止条件：空节点就返回
        if not root:
            return None
        
        # 交换当前节点的左右孩子
        root.left, root.right = root.right, root.left
        
        # 递归翻转左子树
        self.invertTree(root.left)
        
        # 递归翻转右子树
        self.invertTree(root.right)
        
        return root