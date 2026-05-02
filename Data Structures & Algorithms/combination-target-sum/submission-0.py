from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(start, total):
            # 1. 找到一个合法组合
            if total == target:
                ans.append(path.copy())
                return

            # 2. 超过 target，没必要继续
            if total > target:
                return

            # 3. 从 start 开始选，避免顺序重复
            for i in range(start, len(nums)):
                path.append(nums[i])

                # 注意：这里传 i，不是 i + 1
                # 因为 nums[i] 可以重复使用
                dfs(i, total + nums[i])

                path.pop()

        dfs(0, 0)
        return ans