from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. 按起点排序
        intervals.sort()
        
        # 2. 初始化结果，放入第一个区间
        res = [intervals[0]]
        
        # 3. 遍历剩余区间
        for i in range(1, len(intervals)):
            cur = intervals[i]
            last = res[-1]
            # 如果重叠
            if cur[0] <= last[1]:
                last[1] = max(last[1], cur[1])
            else:
                res.append(cur)
        
        return res