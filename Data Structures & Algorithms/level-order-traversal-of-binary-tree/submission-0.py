# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:  # 空树直接返回
            return []
        
        queue = [root]
        ans = []

        while queue:
            level_size = len(queue)  # 当前层有几个节点
            current_level = []       # 存当前层的值

            # 关键：只循环当前层的次数
            for _ in range(level_size):
                node = queue.pop(0)  # 取出队首
                current_level.append(node.val)

                # 左右孩子入队
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # 一层处理完，加入答案
            ans.append(current_level)

        return ans
