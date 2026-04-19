class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        max_len = 0
        char_index = {}
        # 一个字典 char_index，记录 字符: 最后出现的索引

        # 遍历 right 从 0 到 结尾：
        for right in range(len(s)):
            char = s[right]

            # 如果字符重复，并且在窗口内
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1  # 直接跳，不用从头来

            # 更新字符最后出现的位置
            char_index[char] = right

            # 计算当前窗口长度
            current_len = right - left + 1

            # 更新最大值
            max_len = max(max_len, current_len)

        return max_len