import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)  # 复用 add 方法，保证堆大小不超过 k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)  # 弹出最小的，保持堆大小恒为 k
        return self.heap[0]  # 堆顶即第 k 大
        