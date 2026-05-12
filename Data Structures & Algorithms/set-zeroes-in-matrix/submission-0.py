class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_has_zero = first_col_has_zero = False
        for i in matrix:
            if i[0] == 0: #first of every row
                first_col_has_zero = True
                break
        for i in matrix[0]:
            if i == 0: # every one in first row
                first_row_has_zero = True
        
        
        for row in range(1,len(matrix)):
            for col in range(1,len(matrix[0])):
                if matrix[row][col]==0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0


        m = len(matrix) # 行数

        n = len(matrix[0]) # 列数
        
        # then deal with first row, col, set zero
        for i in range(1,m):
            if matrix[i][0] == 0: # 我们检查 i 从 1 到 m-1 的每一行 first one
                matrix[i] = [0]*n # replace with n zero

        for j in range(1,n):
            if matrix[0][j] == 0: # 根据第一行的标记，清零对应的内部列
                for i in range(1,m):
                    matrix[i][j] = 0

        # then based on the two bool, set zero
        if first_row_has_zero:
            matrix[0] = [0]*n
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0 # every first one in row

        # done
        return 