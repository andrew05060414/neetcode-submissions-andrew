from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []

        def dfs(start, remain):
            if remain == 0:
                ans.append(path.copy())
                return

            for i in range(start, len(nums)):
                if nums[i] > remain:
                    break

                path.append(nums[i])
                dfs(i, remain - nums[i])
                path.pop()

        dfs(0, target)
        return ans