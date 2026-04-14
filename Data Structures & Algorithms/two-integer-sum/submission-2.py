class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # go over each int in the list, when find, return
        seen = {}

        for i, num in enumerate(nums):
            need = target - num

            if need in seen:
                return [seen[need],i] # the current index and the other one
            seen[num]=i

    