import copy
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        board = copy.deepcopy(matrix)

        def cvt_row(idx):
            for i in range(0, m):
                board[idx][i] = 0
        def cvt_col(idx):
            for i in range(0, n):
                board[i][idx] = 0
        
        for x in range(n):
            for y in range(m):
                if matrix[x][y] == 0:
                    cvt_row(x)
                    cvt_col(y)
        
        for i in range(n):
            for j in range(m):
                matrix[i][j] = board[i][j]
