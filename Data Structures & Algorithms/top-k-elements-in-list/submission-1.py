import heapq

class Solution:
    def topKFrequent(self, nums, k):
        
        # Step 1: 统计频率
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] = count[num] + 1

        # Step 2: 创建一个空的 heap
        heap = []

        # Step 3: 把 (频率, 数字) 放进 heap
        for num in count:
            freq = count[num]

            heapq.heappush(heap, (freq, num))

            # 如果超过 k 个，就弹出最小的
            if len(heap) > k:
                heapq.heappop(heap)

        # Step 4: 把 heap 里的数字取出来
        result = []

        for item in heap:
            freq = item[0]
            num = item[1]

            result.append(num)

        return result