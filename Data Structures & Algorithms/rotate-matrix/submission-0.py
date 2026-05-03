from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        left = 0
        right = n - 1

        # 一层一层往里转
        while left < right:
            top = left
            bottom = right

            # 当前这一层边长是 right - left + 1
            # 需要做 right - left 组四点交换
            for i in range(right - left):
                # 先存住上边的值，防止被覆盖
                top_left = matrix[top][left + i]

                # 左边 -> 上边
                matrix[top][left + i] = matrix[bottom - i][left]

                # 下边 -> 左边
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # 右边 -> 下边
                matrix[bottom][right - i] = matrix[top + i][right]

                # 原来的上边 -> 右边
                matrix[top + i][right] = top_left

            # 外层转完，进入内层
            left += 1
            right -= 1