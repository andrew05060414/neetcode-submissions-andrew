class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        
        start = 0      # 最长回文的起始索引
        max_len = 1     # 最长回文的长度（至少为1，单个字符）
        
        # 总共有 2n - 1 个中心
        for c in range(2 * n - 1):
            # 计算中心对应的左右指针
            left = c // 2
            right = left + (c % 2)   # 奇数中心：left==right；偶数中心：right=left+1
            
            # 从中心向两边扩展
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            # 扩展结束后，(left+1) 到 (right-1) 是回文串
            cur_len = right - left - 1
            if cur_len > max_len:
                max_len = cur_len
                start = left + 1
        
        return s[start : start + max_len]