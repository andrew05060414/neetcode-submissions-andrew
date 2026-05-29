
from collections import defaultdict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        # 按长度分组
        len2words = defaultdict(set)
        for w in wordDict:
            len2words[len(w)].add(w)
            
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(n):
            if not dp[i]:
                continue
            # 只尝试存在的单词长度，且要保证不超过字符串总长
            for length, words in len2words.items():
                end = i + length
                if end <= n and s[i:end] in words:
                    dp[end] = True
        return dp[n]