class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        res1 = res
        for i in range(res1):
            res ^= i ^ nums[i]
        return res