# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # ans 记录全局最大 path sum
        # 不能初始化成 0，因为树里可能全是负数
        ans = float("-inf")

        def dfs(node):
            nonlocal ans

            # 如果当前节点不存在，它对 parent 的贡献是 0
            # 注意：这里的 0 不是一条真正的 path
            # 它只是表示“这边没有节点可以接”
            if not node:
                return 0

            # 先递归算左子树能给当前 node 贡献多少
            left_gain = dfs(node.left)

            # 再递归算右子树能给当前 node 贡献多少
            right_gain = dfs(node.right)

            # 如果某边贡献是负数，就不要它
            # 因为接上负数只会让 path sum 更小
            left_gain = max(0, left_gain)
            right_gain = max(0, right_gain)

            # 当前 node 作为“拐点”
            # path 可以是：left -> node -> right
            # 这个 candidate 可以更新全局答案
            candidate = node.val + left_gain + right_gain
            ans = max(ans, candidate)

            # 但是返回给 parent 的时候，不能左右都带
            # 因为 parent 接上来以后，path 不能分叉
            # 所以只能返回 node + 左边 或 node + 右边 中更大的那个
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return ans