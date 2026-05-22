class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        # break down into two cases:
        # rob 1, end at n-1
        prev2 = nums[0]                     # dp[i-2]
        prev1 = max(nums[0], nums[1])       # dp[i-1]
        for i in range(2, n-1):
            curr = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = curr
        
        a = prev1
        # skip 1, end at n
        prev2b = nums[1]                     # dp[i-2]
        prev1b = max(nums[1], nums[2])       # dp[i-1]
        for i in range(3, n):
            curr = max(prev1b, prev2b + nums[i])
            prev2b = prev1b
            prev1b = curr
        # then max(a,b)
        b = prev1b

        return max(a,b)