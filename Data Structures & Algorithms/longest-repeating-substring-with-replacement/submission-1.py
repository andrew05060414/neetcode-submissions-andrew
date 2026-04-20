class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 1. 初始化变量
        count = [0] * 26  # 统计26个大写字母出现次数
        left = 0          # 左指针
        max_len = 0       # 答案：最长长度
        max_count = 0     # 窗口内出现最多的字符次数

        # 2. 右指针遍历整个字符串
        for right in range(len(s)):
            # --- 右指针进窗口 ---
            alpha = ord(s[right])- ord('A') # the number of the alphabet
            count[alpha] += 1

            # 更新窗口内最大字符数
            max_count = max(max_count, count[alpha])

            # --- 判断窗口是否合法：不合法就移动左指针 ---
            # 窗口长度 - 最多字符数 > k → 需要改的太多了
            while (right - left + 1) - max_count >k:
                # 左指针出窗口
                left_idx = ord(s[left]) - ord('A')
                count[left_idx] -= 1
                left += 1

            # --- 窗口合法，更新最长长度 ---
            max_len = max(max_len, right-left+1)

        return max_len