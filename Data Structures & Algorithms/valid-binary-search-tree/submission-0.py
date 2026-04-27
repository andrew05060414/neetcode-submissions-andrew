# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, low, high):
            # 1. 如果 node 是 None，说明这条分支没问题
            if not node:
                return True

            # 2. 如果 node.val 不在 (low, high) 范围内，说明不是 BST
            if not low < node.val < high:
                return False
            # 3. 检查左子树
            #    左子树所有值必须 < node.val
            #    所以 high 变成 node.val
            left_ok =  valid(node.left, low, node.val)

            # 4. 检查右子树
            #    右子树所有值必须 > node.val
            #    所以 low 变成 node.val
            right_ok =  valid(node.right, node.val, high)
            # 5. 左右都合法，当前子树才合法
            return left_ok  and right_ok
        return valid(root, float("-inf"), float("inf"))