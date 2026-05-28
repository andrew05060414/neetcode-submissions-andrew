class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = ans = nums[0]
        for num in nums[1:]:
            old_max = cur_max
            cur_max = max(num, cur_max * num, cur_min * num)
            cur_min = min(num, old_max * num, cur_min * num)
            ans = max(ans, cur_max)
        return ans