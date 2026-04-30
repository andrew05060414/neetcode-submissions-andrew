# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(pre,ino):
            if not pre:
                return None

            # Solve it with slicing 
            root = pre[0]
            ans = TreeNode(root)
            
            mid = ino.index(root)
            # resursive
            left_in = ino[:mid]
            right_in = ino[mid+1:]

            left_size = len(left_in)
            left_pre = pre[1:left_size+1]
            right_pre = pre[1+left_size:]

            ans.left = build(left_pre,left_in)
            ans.right = build(right_pre, right_in)

            return ans

        return build(preorder,inorder)


