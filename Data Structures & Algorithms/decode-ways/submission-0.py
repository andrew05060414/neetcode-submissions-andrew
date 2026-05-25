class Solution:
    def numDecodings(self, s: str) -> int:
        # like taking steps, one or two number(stair) at a time
        n = len(s)
        if s[0] == '0':
            return 0
        
        dp = [0] * n
        dp[0] = 1  # 第一个字符合法
        
        for i in range(1, n):
            # 单数字
            if s[i] != '0':
                dp[i] += dp[i - 1]
            # 双数字
            two_digit = int(s[i - 1 : i + 1])
            if 10 <= two_digit <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        
        return dp[-1]