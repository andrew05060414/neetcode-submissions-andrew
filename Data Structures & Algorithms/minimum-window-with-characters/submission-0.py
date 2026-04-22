from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. 统计 t 里面的字符需求
        count_t = defaultdict(int)
        for c in t:
            count_t[c] += 1
        
        required = len(count_t)  # 需要匹配多少种字符
        window = defaultdict(int)
        
        left = 0
        matched = 0             # 已经匹配成功的种类数
        min_len = float('inf')
        res_left = 0

        # 2. 右指针一直走
        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            # 如果这个字符刚好达到要求，matched +1
            if c in count_t and window[c] == count_t[c]:
                matched += 1

            # 3. 窗口合法 → 开始缩左（求最小！）
            while matched == required:
                # 记录最小窗口
                cur_len = right - left + 1
                if cur_len < min_len:
                    min_len = cur_len
                    res_left = left

                # 左指针移出
                left_c = s[left]
                if left_c in count_t and window[left_c] == count_t[left_c]:
                    matched -= 1
                window[left_c] -= 1
                left += 1

        # 4. 返回结果
        if min_len == float('inf'):
            return ""
        return s[res_left : res_left + min_len]