class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for x in range(1, amount+1):
            # for coin in coins
            for c in coins:
                # each coin is taking x step 
                if x >= c: # did not reach amount
                    dp[x] = min(dp[x],dp[x-c]+1)
            # do dp here
            # stack while value < amount. 
        
        return dp[amount] if dp[amount] != float('inf') else -1