from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        # print(rows)
        cols = len(grid[0])
        # print(cols)
        count = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c]="0"

            while q: # when there is still q
                row, col = q.popleft()
                
                for dr,dc in directions:
                    nr = row + dr
                    nc = col + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols: #between 0 and len-1
                        if grid[nr][nc] == "1":
                            grid[nr][nc]="0"
                            q.append((nr,nc))
            return 
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r,c)
                    


        return count