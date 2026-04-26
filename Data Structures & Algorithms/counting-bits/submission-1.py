class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_1(x):
            count = 0
            while x:
                # 看最后一位是不是 1
                count += x & 1
                # 右移一位
                x = x >> 1
            return count
        res = []
        for i in range(n+1):
            res.append(count_1(i))
        return res