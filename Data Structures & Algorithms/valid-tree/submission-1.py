class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        stack = [0]

        while stack:
            node = stack.pop()

            if node in visited:
                continue

            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    stack.append(nei)

        return len(visited) == n