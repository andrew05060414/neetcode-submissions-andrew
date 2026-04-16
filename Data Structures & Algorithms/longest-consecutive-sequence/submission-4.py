class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0

        for num in num_set:
            if num-1 in num_set:
                continue

            current_num = num
            current_length = 1

            while current_num+1 in num_set:
                current_num += 1
                current_length += 1

            best = max(best, current_length)

        return best
