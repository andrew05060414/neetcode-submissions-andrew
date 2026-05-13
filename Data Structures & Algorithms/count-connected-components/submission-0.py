from collections import deque
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 构建邻接表
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)  # 无向图，双向连接
        
        visited = [False] * n
        count = 0
        
        for i in range(n):
            if not visited[i]:
                count += 1
                # BFS
                queue = deque([i])
                visited[i] = True
                while queue:
                    node = queue.popleft()
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
        
        return count