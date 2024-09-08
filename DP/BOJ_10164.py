# S2, 격자상의 경로
n, m, num = map(int, input().split())

board = [[0] * m for _ in range(n)]
cnt = 1
target = [-1, -1]
for i in range(n):
    for j in range(m):
        board[i][j] = cnt
        if num == cnt:
           target[0] = i
           target[1] = j 
        cnt += 1


dp = [[1] * m for _ in range(n)]
if sum(target) != -2:
    for i in range(1, target[0] + 1):
        for j in range(1, target[1] + 1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    for i in range(target[0], n):
        dp[i][target[1]] = dp[target[0]][target[1]]
    for i in range(target[1], m):
        dp[target[0]][i] = dp[target[0]][target[1]]
        
    for i in range(target[0] + 1, n):
        for j in range(target[1] + 1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
else:
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]


print(dp[n-1][m-1])