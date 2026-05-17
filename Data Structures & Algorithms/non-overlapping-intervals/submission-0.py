class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # 按结束时间升序
        count = 1          # 保留的数量
        last_end = intervals[0][1]    # 上一个保留区间的结束时间

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= last_end:
                count += 1
                last_end = end
            # 否则重叠，需要移除，什么都不做，继续

        return len(intervals) - count