class Solution:
    def countSubstrings(self, s: str) -> str:
        n = len(s)
        count = 0 
        
        # 总共有 2n - 1 个中心
        for c in range(2 * n - 1):
            # 计算中心对应的左右指针
            left = c // 2
            right = left + (c % 2)   # 奇数中心：left==right；偶数中心：right=left+1
            
            # 从中心向两边扩展
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1            # 每扩展成功一步，就是一个回文
                left -= 1
                right += 1
            
        return count