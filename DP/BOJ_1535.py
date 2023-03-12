# 안녕, S2, DP
# 브루트포스
# Knapsack Pro

from sys import stdin

# 1. 0-1 Knapsack 풀이            = 가져가거나, 버리거나
# max(i-1 개의 물건들을 갖고 구한 전 단계의 값, i 번째 물건만큼의 무게를 비웠을 때의 값 + i 번째 물건

n = int(stdin.readline())
hp = [0] + list(map(int,stdin.readline().split()))
happy = [0] + list(map(int,stdin.readline().split()))

dp = [[0]*101 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1, 101):     # 체력 한계치가 100
        if hp[i] <= j:          # 현재 남은 체력이 다음 들어올 값보다 많다면 : 다음 들어올 값=hp[i]
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-hp[i]] + happy[i])     # 이전 체력에서 인사하면서 체력을 깎고, happy값을 더한다.
        else:
            dp[i][j] = dp[i-1][j]       # 인사하면 뒤지는 체력일 때, 이전 체력을 그대로 유지하면서 happy를 pass한다.

print(dp[n][99])                # 체력이 1 남았을 때가 기준

# ------------------------- 1차원 배열을 이용한 풀이

hp = list(map(int,stdin.readline().split()))
happy = list(map(int,stdin.readline().split()))

res = [0]*101           # index = 체력
for i in range(1, n+1):
    s = hp[i-1]         # 한명 만날때 마다 필요한 체력(깎이는 체력)
    p = happy[i-1]      # 얻는 기쁨

    for j in range(100, 0, -1):     # 체력을 100부터 깎아나간다는 마인드
        if j > s:                   # 남은 체력이 더 많을 때,
            res[j] = max(res[j], res[j-s] + p)      # 해당 체력 index일때의 p 값을 더해줌

print(res[-1])          # 제일 마지막 값
