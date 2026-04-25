class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # 看最后一位是不是 1
            count += n & 1
            # 右移一位
            n = n >> 1
        return count