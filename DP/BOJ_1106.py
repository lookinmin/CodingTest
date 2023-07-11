# 호텔, G5, dp-knapsack problem

from sys import stdin

c, n = map(int, stdin.readline().split())
# 고객을 C 명 늘려야하고 N개의 도시에 홍보 가능
arr = []
INF = int(1e9)
cnt = 0
for _ in range(n):
    cost, people = map(int, stdin.readline().split())
    arr.append([cost,people])
    cnt = max(cnt, people)

# 범위 : c + 최대 인원 값 + 1
dp = [INF] * (c + cnt + 1)
dp[0] = 0

for cost, people in arr:
    for i in range(people, c + cnt + 1):
        dp[i] = min(dp[i-people] + cost, dp[i])


print(min(dp[c:]))





