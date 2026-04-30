# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {val: i for i, val in enumerate(inorder)}

        def build(pre_l, pre_r, in_l, in_r):
            if pre_l >= pre_r:
                return None

            root_val = preorder[pre_l]
            node = TreeNode(root_val)

            mid = idx[root_val]
            left_size = mid - in_l

            # left recursion
            node.left = build(pre_l + 1, pre_l + 1 + left_size, in_l, mid)

            # right recursion
            node.right = build(pre_l + 1 + left_size, pre_r, mid + 1, in_r)
            return node
        return build(0,len(preorder),0,len(inorder))