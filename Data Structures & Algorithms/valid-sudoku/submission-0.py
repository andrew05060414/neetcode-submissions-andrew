class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 初始化行、列、九宫格的标记数组
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == '.':
                    continue
                num = int(cell) - 1  # 数字 1-9 映射到索引 0-8

                # 计算属于哪个九宫格 (0-8)
                box_index = (i // 3) * 3 + (j // 3)

                # 检查是否重复
                if rows[i][num] or cols[j][num] or boxes[box_index][num]:
                    return False

                # 标记已出现
                rows[i][num] = True
                cols[j][num] = True
                boxes[box_index][num] = True

        return True