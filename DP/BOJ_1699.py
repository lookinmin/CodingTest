# 제곱수의 합, S2, DP
# bottom-up

n = int(input())
dp = [0 for i in range(n+1)]
square = [i**2 for i in range(1, 317)]

# i = 1~n까지의 숫자
# j = i보다 작거나 같은 제곱수

for i in range(1, n+1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i-j])       # ex) i=16이면 j=1,4,9,16
    dp[i] = min(s) + 1          # dp[16] = min(dp[16-1], dp[16-4], dp[16-9], dp[16-16]) + 1 == 0 + 1 따라서 dp[16] = 1

print(dp[n])