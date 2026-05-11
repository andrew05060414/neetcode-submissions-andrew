class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []

        m = len(matrix)
        n = len(matrix[0])

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        while top <= bottom and left <= right:
            # 1. 走上边：从左到右
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # 2. 走右边：从上到下
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # 3. 走下边：从右到左
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            # 4. 走左边：从下到上
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res