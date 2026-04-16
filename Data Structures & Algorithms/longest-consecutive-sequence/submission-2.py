class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums.sort()
        current = 0
        best = 0
        prev = -99999999999999999999
       
        print(nums)
        
        for num in nums: #loop over

            # if consecutive
            if num == prev + 1:
                current +=1
                #count +=1
            elif num == prev:
                best = max(best,current+1)
            else: 
                best = max(best,current+1)
                # print(best, current)
                current = 0
            prev = num
        
        best = max(best,current+1)
        return best