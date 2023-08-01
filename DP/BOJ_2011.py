# 암호코드, G5, DP

from sys import stdin

origin = list(map(int,stdin.readline().rstrip()))
k = len(origin)

dp = [0] * (k+1)

if origin[0] == 0:
    print(0)
else:
    origin = [0] + origin
    dp[0] = dp[1] = 1
    for i in range(2, k+1):
        if origin[i] > 0:
            dp[i] += dp[i-1]
        tmp = 10*origin[i-1] + origin[i]
        if 10 <= tmp <= 26:
            dp[i] += dp[i-2]

    print(dp[k] % 1000000)

# words = {}
# for i in range(26):
#     words[chr(ord('A') + i)] = i+1

# 1~26만 가능, 0이 뜨면 무조건 10, 20
# 1. 현재 자리 수 > 0 -> 이전 dp값 더함
# 이전 dp가 가진 방법들 + 한 자리수 추가
# ex) 2 5 1 1 4 -> 2 5 1 1 / 4 일 때(탐색이 4), -> [2, 5, 1, 1], [25, 1, 1], [2, 5, 11], [25, 11] 이렇게 4가지에 뒤에 하나 독립적
# 즉 4가지 (+1이 아님)

# 2. 이전 자리수와 현재 자리수를 두자리 수로 본다 -> 전 전 dp값 더함
# ex) 2 5 1 / 1 4 ->[2, 5, 1], [25, 1] 2가지
# 즉 2가지 추가

