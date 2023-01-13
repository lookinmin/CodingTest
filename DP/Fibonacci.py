# 피보나치 DP
# 시간 복잡도 = O(n)

# Top-down
d = [0] * 100
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

# ------------------------------------------------------------ #

# Bottom-up
dp = [0] * 100
dp[1] = dp[2] = 1
n = 99      # 구하려고 하는 n의 값

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
