class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. 长度判断
        if len(s) != len(t):
            return False
        # 2. count dict
        count1 = {}
        count2 = {}
        # 3. 遍历 s
        for char in s:
            if char in count1:
                count1[char] += 1
            else:
                count1[char] = 1

        # 4. 遍历 t
        for char in t:
            if char in count2:
                count2[char] += 1
            else:
                count2[char] = 1

        # 5. 判断是否全为0
        return count1 == count2