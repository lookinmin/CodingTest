from sys import stdin
n, m, k = map(int, stdin.readline().split())
lst1 = list(map(int, stdin.readline().split()))
lst2 = list(map(int, stdin.readline().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]
res = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if lst1[i - 1] == lst2[j - 1]:
            dp[i][j] = dp[i-1][j-1] + 1
            res = max(res, dp[i][j])

print(res)