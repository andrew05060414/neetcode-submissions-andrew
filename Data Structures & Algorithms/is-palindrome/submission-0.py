class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            # 跳过左边非法字符
            while left < right and not s[left].isalnum():
                left += 1

            # 跳过右边非法字符
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() == s[right].lower():
                left += 1
                right -=1
            else:
                return False

        return True