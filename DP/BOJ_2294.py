# 동전 2, G5, DP

from sys import stdin

n, k = map(int, stdin.readline().split())
coins = []

for i in range(n):
    coin = int(stdin.readline())
    coins.append(coin)

dp  = [10001] * (k+1)
dp[0] = 0

# 동전이 c1, c2, c3 일 때,
# dp[n] = dp[n-c1], dp[n-c2], dp[n-c3] 중 가장 min값 + 1(1개를 더 쓰는거니까)
# 즉, c1을 사용한다면 n-c1원을 만든 동전의 수 + c1동전 1개


for i in coins:         # 각 화폐단위
    for j in range(i, k + 1):       # 금액k까지
        if dp[j] > 0:
            dp[j] = min(dp[j],dp[j-i] + 1)          #dp[j]의 초기값은 10001, 무조건 dp[j-coin] + 1이 선택된다.

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
