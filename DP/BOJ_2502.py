# 떡 먹는 호랑이, S1, DP
# 어제 받은 떡 + 그저께 받은 떡
# day1 = x, day2 = y
# day3 = x+y -> x+2y -> 2x+3y -> 3x+5y -> 5x+8y -> 8x+13y

from sys import stdin

D, K = map(int,stdin.readline().split())
dp=[0] * D
dp[0] = 1                   # 초기값을 1이라 가정
dp[1] = 1

while 1:
    for i in range(2, D):
        dp[i] = dp[i - 1] + dp[i - 2]       # 변화하는 초기값에 따라 다른 dp 배열을 만들어야 함

    if dp[D-1] == K:
        print(dp[0])
        print(dp[1])
        break
    elif dp[-1] > K:        # 제일 마지막 수가 K보다 크다면
        dp[0] += 1          # 초기값을 하나씩 증가시켜서 확인
        dp[1] = dp[0]
    else:
        dp[1] += 1          # K보다 작다면, 둘째날에 주는 것만 +1
