class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2   # 避免溢出，等价于 (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:           # target 在右边，收缩左边界
                left = mid + 1
            else:                              # target 在左边，收缩右边界
                right = mid - 1
        return -1