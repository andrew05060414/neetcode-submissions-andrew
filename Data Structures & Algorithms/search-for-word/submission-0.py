class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r, c, i):
            # TODO 1: 如果 i 已经等于 len(word)，说明匹配完了
            if i == len(word):
                return True
            # TODO 2: 如果越界，返回 False
            if  0 > r or r >= rows or 0 > c or c>= cols:
                return False
            # TODO 3: 如果这个格子已经用过，返回 False
            if board[r][c] == "#":
                return False
            # TODO 4: 如果 board[r][c] != word[i]，返回 False
            if board[r][c] != word[i]:
                return False
            # TODO 5: 标记当前格子 visited
                # got what we want
            temp = board[r][c]
            board[r][c] = "#"
            # TODO 6: 去四个方向继续找 i + 1
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1):
                    board[r][c] = temp
                    return True
                    
            # TODO 7: 回溯，取消 visited
            board[r][c] = temp
            # TODO 8: 返回四个方向有没有成功
            return False
        for r in range(rows):
            for c in range(cols):
                # 如果从这个格子出发能找到 word，返回 True
                if dfs(r, c, 0):
                    return True
        return False