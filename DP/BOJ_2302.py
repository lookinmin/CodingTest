# 극장 좌석, S1, DP
# 접근 방식
# 합의 법칙 = 두 사건이 동시에 일어나지 않을 경우 -> 더한다
# 곱의 법칙 = 두 사건이 동시에 일어날 경우 -> 곱한다.

from sys import stdin
n = int(stdin.readline().strip())   # 총 좌석의 수
m = int(stdin.readline().strip())   # 고정석 갯수
vip = [int(stdin.readline().strip()) for _ in range(m)]

dp = [1, 1, 2]
for i in range(3, n + 1):
    # 점화식: 자리를 옮기거나, 옮기지 않거나
    dp.append(dp[i - 2] + dp[i - 1])

res = 1
if m >= 1:
    pre = 0
    for i in range(m):
        idx = vip[i] - 1 - pre
        res *= dp[idx]       # 총 좌석을 인원에 맞는 그룹 수로 나누어 dp 계산
        pre = vip[i]
    res *= dp[n-pre]
else:
    res = dp[n]

print(res)

