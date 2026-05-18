class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_max = cur_max = ans = -1001
        for num in nums:
            cur_max = max(prev_max + num, num)
            # print(prev_max + num, num, cur_max)
            ans = max(ans, cur_max)
            prev_max = cur_max
        return ans