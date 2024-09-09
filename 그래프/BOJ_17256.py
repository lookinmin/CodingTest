from sys import stdin

n = int(input())
board = [stdin.readline().split() for _ in range(n)]

max_res = -float('inf')
min_res = float('inf')

def dfs(x, y, exp):
    global max_res, min_res

    if x == y == n - 1:
        max_res = max(max_res, eval(exp))
        min_res = min(min_res, eval(exp))
        return
    
    try:
        dfs(x + 1, y, exp + board[x+1][y] if (x+y) % 2 == 0 else str(eval(exp + board[x + 1][y])))
    except:
        pass
    try:
        dfs(x, y + 1, exp + board[x][y + 1] if (x+y) % 2 == 0 else str(eval(exp + board[x][y + 1])))
    except:
        pass

dfs(0, 0, board[0][0])
print(max_res, min_res)