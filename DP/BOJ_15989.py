# 1,2,3 더하기 4, S1, DP
# 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 합을 이루고 있는 수의 순서만 다른 것은 같은 것으로 친다
from sys import stdin

T = int(stdin.readline())

dp = [1] * 10001        # 오직 1만써서 합을 나타내는 방법은 1가지씩 있음

for i in range(2, 10001):
    dp[i] += dp[i-2]        # 2를 사용하는 경우의 수 추가

for i in range(3, 10001):
    dp[i] += dp[i-3]

for _ in range(T):
    n = int(stdin.readline())
    print(dp[n])

