class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            last_bit = n & 1
            res = res << 1
            res = res | last_bit
            n = n >> 1
        return res