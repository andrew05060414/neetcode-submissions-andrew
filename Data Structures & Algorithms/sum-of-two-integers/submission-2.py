class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        max_int = 0x7fffffff
        while b != 0:
            sum_without_carry = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = sum_without_carry
            b = carry

        return a if a<=max_int else ~(a ^ mask)
        