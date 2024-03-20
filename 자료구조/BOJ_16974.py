# 레벨 햄버거, S1, 재귀-DP

from sys import stdin

n, x = map(int,stdin.readline().split())

# 레벨 n
# 아래 k 장 eat
# 패티(P)의 수?
# dp = []
# dp.append([1])
# dp.append([0, 1, 1, 1, 0])
# dp.append([0] + dp[1] + [1] + dp[1] + [0])
#
# for i in range(2, n+1):
#     dp.append([0] + dp[i] + [1] + dp[i] + [0])


# print(dp[n][:x+1].count(1))

# 메모리 초과

burger = [1] * 51
patty = [1] * 51

for i in range(1, n+1):
    burger[i] = 1 + burger[i-1] + 1 + burger[i-1] + 1
    patty[i] = patty[i-1] + 1 + patty[i-1]


def eat(n, x):
    if n == 0:
        return x
    if x == 1:      # 시작은 B
        return 0
    elif x <= 1 + burger[n-1]:          # 가운데보다 작은 수까지
        return eat(n-1, x-1)
    elif x == 1 + burger[n-1] + 1:      # 딱 가운데 패티까지
        return patty[n-1] + 1
    elif x <= burger[n-1] + burger[n-1] + 1 + 1:        # 가운데 보다는 많이, 끝까지는 아님
        return patty[n-1] + 1 + eat(n-1, (x-(burger[n-1] + 2)))     # 가운데 이상 먹었으니 절반은 더해주고 나머지는 재귀적으로
    else:           # 끝까지 다먹음
        return patty[n]


print(eat(n, x))


