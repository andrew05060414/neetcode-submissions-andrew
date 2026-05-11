class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix)
        n = len(matrix[0])

        res = []
        visited = set()

        # 右、下、左、上
        dirs = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        r = 0
        c = 0
        direction = 0

        for _ in range(m * n):
            res.append(matrix[r][c])
            visited.add((r, c))

            dr, dc = dirs[direction]
            nr = r + dr
            nc = c + dc

            # 如果下一步越界，或者下一步已经走过，就转方向
            if (
                nr < 0 or nr >= m or
                nc < 0 or nc >= n or
                (nr, nc) in visited
            ):
                direction = (direction + 1) % 4
                dr, dc = dirs[direction]
                nr = r + dr
                nc = c + dc

            r = nr
            c = nc

        return res