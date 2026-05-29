class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)          # 转成集合，O(1) 查找
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True                     # 空字符串可以拆分

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break                # 一旦找到一种拆分方式就跳出，减少计算
        return dp[n]