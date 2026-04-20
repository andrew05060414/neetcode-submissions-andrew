class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        max_len = 0
        max_count = 0

        for right in range(len(s)):
            # 右指针进窗口
            c = s[right]
            count[ord(c) - ord('A')] += 1
            # 当前窗口最多字符
            max_count = max(max_count, count[ord(c) - ord('A')])

            # 窗口不合法，左移
            while (right - left + 1) - max_count > k:
                left_c = s[left]
                count[ord(left_c) - ord('A')] -= 1
                left += 1

            # 更新答案
            max_len = max(max_len, right - left + 1)


        return max_len