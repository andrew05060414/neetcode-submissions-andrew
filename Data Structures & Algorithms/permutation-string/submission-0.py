class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        # 统计 s1 的字符频率，以及 s2 第一个窗口的频率
        count1 = [0] * 26
        count2 = [0] * 26
        
        for i in range(n1):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        # 检查第一个窗口
        if count1 == count2:
            return True
        
        # 滑动窗口：窗口长度固定为 n1
        for i in range(n1, n2):
            # 加入右边新字符
            count2[ord(s2[i]) - ord('a')] += 1
            # 移除左边旧字符
            count2[ord(s2[i - n1]) - ord('a')] -= 1
            # 比较
            if count1 == count2:
                return True
        
        return False