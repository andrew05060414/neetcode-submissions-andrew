class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(n):
            if not dp[i]:
                continue
            for w in wordSet:          # 或者预先按长度分组优化
                end = i + len(w)
                if end <= n and s[i:end] == w:
                    dp[end] = True
        
        return dp[n]