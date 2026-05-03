

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 如果没有会议，不需要房间
        if not intervals:
            return 0

        # 先按会议开始时间排序
        intervals.sort(key=lambda x: x.start)

        # heap 里存的是每个正在使用的房间的结束时间
        min_heap = []

        for interval in intervals:
            # 如果 heap 不为空，并且当前会议的开始时间
            # 大于等于最早结束的会议时间
            # 说明这个房间可以复用
            if min_heap and interval.start >= min_heap[0]:
                heapq.heappop(min_heap)

            # 不管是复用旧房间，还是开新房间
            # 当前会议都会占用一个房间直到 interval.end
            heapq.heappush(min_heap, interval.end)

        # heap 里剩下多少个 end time
        # 就代表最多同时占用过多少个房间
        return len(min_heap)