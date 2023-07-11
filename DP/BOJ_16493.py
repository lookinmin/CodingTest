# 최대 페이지 수, S2, dp-knapsack

from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [[0,0]]

for _ in range(m):
    day, page = map(int, stdin.readline().split())
    arr.append([day, page])

dp = [[0] * (n+1) for _ in range(m+1)]

for i in range(1, m + 1):       # 챕터 (m개)
    for j in range(1, n + 1):   # 남은 날짜
        day = arr[i][0]         # m번째 날의 소요되는 날짜
        page = arr[i][1]        # m번째 날의 읽을 수 있는 page

        if j - day < 0:             # 읽을 수 없음 (남은 날짜보다 요구되는 날짜가 더 많음)
            dp[i][j] = dp[i-1][j]
        else:                   # 읽을 수 있음
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - day] + page)
                        # max(챕터를 읽지 않는 경우, 읽는 경우)
print(dp[m][n])