from sys import stdin

n = int(stdin.readline())
board = [[] for _ in range(n)]

for i in range(n):
    board[i] = list(map(int, stdin.readline().split()))

INF = int(1e9)
dp = [[INF] * 3 for _ in range(n + 1)]

dp[0][1] = 0

for i in range(1, n + 1):
    if board[i-1][0] == 0:
        dp[i][0] = min(dp[i-1][0], dp[i-1][1] + 1, dp[i-1][2] + 2)
    if board[i-1][1] == 0:
        dp[i][1] = min(dp[i - 1][0] + 1, dp[i - 1][1], dp[i - 1][2] + 1)
    if board[i-1][2] == 0:
        dp[i][2] = min(dp[i - 1][0] + 2, dp[i - 1][1] + 1, dp[i - 1][2])

print(min(dp[n]))

# 시간복잡도 O(n)
# 공간복잡도 O(n)
# board 배열 선언 -> 2차원 리스트 (n * 3) = n
# dp 배열 선언 -> 2차원 리스트(n+1 * 3) = n