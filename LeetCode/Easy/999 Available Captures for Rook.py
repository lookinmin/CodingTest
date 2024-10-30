class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        x = -1
        y = -1

        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x = i
                    y = j
                    break
        
        def check(x, y):
            # 오
            cnt = 0
            for i in range(y + 1, 8):
                if board[x][i] == 'p':
                    cnt += 1
                    break
                elif board[x][i] == 'B':
                    break
            
            # 왼
            for i in range(y - 1, -1, -1):
                if board[x][i] == 'p':
                    cnt += 1
                    break
                elif board[x][i] == 'B':
                    break
            # 위
            for i in range(x - 1, -1 , -1):
                if board[i][y] == 'p':
                    cnt += 1
                    break
                elif board[i][y] == 'B':
                    break
            # 아래
            for i in range(x + 1, 8):
                if board[i][y] == 'p':
                    cnt += 1
                    break
                elif board[i][y] == 'B':
                    break
            return cnt

        res = check(x, y)
        return res