class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # go over each int in the list, when find, return

        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums[index1+1:],start=index1+1):
                x = num1 + num2 
                if x == target:
                    return [index1,index2]


    