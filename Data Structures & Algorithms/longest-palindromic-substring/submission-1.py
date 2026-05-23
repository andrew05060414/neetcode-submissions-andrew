class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        
        # dp[i][j] 表示 s[i...j] 是否回文
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1
        
        # 所有单个字符都是回文
        for i in range(n):
            dp[i][i] = True
        
        # 检查长度为 2 的子串
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2
        
        # 按长度从 3 到 n 逐步扩展
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # 两端相等，且中间子串是回文
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_len = length
        
        return s[start : start + max_len]