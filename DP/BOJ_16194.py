# 카드 구매하기 2, 실버1, DP

# dp[1] = 1을 만드는 방법은 1번 카드 1개를 쓰는 방법뿐이다.
# dp[2] = 2를 만드는 방법은 2번 카드 1개, 혹은 1번 카드 2개를 쓰는 것 중 큰 수 이다.
# dp[3] = 3을 만드는 방법은 3번 카드 1개, 혹은 1과 dp[2]를 쓰는 것 중 큰 수이다. 여기서 1,1,1로 3을 만드는 경우, 1,2로 3을 만드는 경우는 dp[2]에서 처리가 끝난 것이다.
# ...
# dp[n] = n을 만드는 방법은 n번 카드 1개, 혹은 1과 dp[n-1], 혹은 dp[2]와 dp[n-2], ..dp[i]와 dp[n-i]를 만드는 것 중 중 큰 수이다.

from sys import stdin

n = int(stdin.readline())
p = [0] + list(map(int, stdin.readline().split()))
dp = [0] * (n+1)
dp[1] = p[1]
dp[2] = min(p[2], p[1]*2)

for i in range(3 ,n+1):
    dp[i] = p[i]
    for j in range(1, i//2 + 1):
        dp[i] = min(dp[i], dp[j] + dp[i-j])

print(dp[n])