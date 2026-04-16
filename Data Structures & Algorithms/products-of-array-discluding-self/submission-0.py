class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1] * length
        right = [1] * length
        answer = [0] * length


        left[0] = 1
        for i in range(1, length):
            left[i] = left[i-1]*nums[i-1]
            #print(f"left i is {i, left[i]}")

        right[length - 1] = 1
        for i in range(length - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
            #print(f"right i is {i, right[i]}")
        
        # answer[i] = left[i] * right[i]
        #print(left,right)
        index = 0
        for i in range(length):
            answer[i] = left[i] * right[i]
        return answer
            

