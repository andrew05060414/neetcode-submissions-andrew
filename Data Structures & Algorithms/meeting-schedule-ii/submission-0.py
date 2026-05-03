

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # events 用来记录“时间点发生了什么变化”
        # (time, +1) 表示这个时间有会议开始，需要多一个房间
        # (time, -1) 表示这个时间有会议结束，释放一个房间
        events = []

        for interval in intervals:
            # 会议开始：房间数量 +1
            events.append((interval.start, 1))

            # 会议结束：房间数量 -1
            events.append((interval.end, -1))

        # 按时间从小到大排序
        # 如果时间相同，Python 会比较 tuple 的第二个值
        # 所以 (8, -1) 会排在 (8, 1) 前面
        # 这刚好处理了 (0,8), (8,10) 不冲突的情况
        events.sort()

        rooms = 0  # 当前正在使用的房间数
        ans = 0    # 历史上同时需要的最多房间数

        for time, change in events:
            # 根据当前事件更新房间数
            rooms += change

            # 更新最大房间需求
            ans = max(ans, rooms)

        return ans