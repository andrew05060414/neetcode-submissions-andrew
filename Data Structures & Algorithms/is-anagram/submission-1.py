class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. 长度判断
        if len(s) != len(t):
            return False
        # 2. count dict
        count1 = [0] * 26
        count2 = [0] * 26
        # 3. 遍历 s
        for c in s:
            idx = ord(c) - ord('a')
            count1[idx] += 1

        # 4. 遍历 t
        for c in t:
            idx = ord(c) - ord('a')
            count2[idx] += 1

        # 5. 判断是否全为0
        return count1 == count2