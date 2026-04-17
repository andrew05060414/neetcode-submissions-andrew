class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        def twoSum(nums: List[int], target: int):
            seen = {}
            ans = []
            for num in nums:
                need = target - num
                if need in seen:
                    ans.append([need, num])
                seen[num] = 1
            return ans

        for i in range(len(nums)):
            num = nums[i]
            nums_minus = nums[i+1:]
            pairs = twoSum(nums_minus, -num)

            for pair in pairs:
                triplet = tuple(sorted([num] + pair))
                answer.add(triplet)
        
        return list(answer)