class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums.sort()

        current = 1
        best = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: #same
                continue
            elif nums[i] == nums[i - 1] + 1: # cur = prev + 1
                current += 1
            else:
                best = max(best, current) 
                current = 1

        best = max(best, current)
        return best