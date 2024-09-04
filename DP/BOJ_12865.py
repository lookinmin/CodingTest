# G5, 평범한 배낭
# 0-1 배낭

from sys import stdin
n, k = map(int, stdin.readline().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    w, v = map(int, stdin.readline().split())
    for j in range(1, k + 1):  # 무게 제한까지
        if w > j:
            # 현재 넣으려는 아이템의 무게 > 지금 채우려는 가방의 한계치
            dp[i][j] = dp[i - 1][j]
            # 덮어씀
        else:
            # 넣을 수 있음 -> 가치 비교
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            # max(이전거 그대로, 지금거 넣기)
    print(dp)
print(dp[n][k]) 
