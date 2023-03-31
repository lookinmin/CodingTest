# 돌 게임2, S4, DP
# 돌은 1개 or 3개

from sys import stdin

n = int(stdin.readline())
# 남은 돌이 2 -> 지금 돌 드는 애가 무조건 이김
# 남은 돌이 3 -> 지금 돌 드는 애가 무조건 짐
# 남은 돌이 4 -> 지금 돌 드는 애가 무조건 이김
# n이 홀수 = 상근이가 무조건 진다
# n이 짝수 = 창영이가 무조건 진다

if n % 2 == 0:
    print("SK")
else:
    print("CY")