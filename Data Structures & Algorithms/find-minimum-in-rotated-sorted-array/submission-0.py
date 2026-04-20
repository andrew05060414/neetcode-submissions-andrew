class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # 核心二分判断
            if nums[mid] < nums[right]:
                # 最小值在左边
                right = mid
            else:
                # 最小值在右边
                left = mid + 1
                
        return nums[left]