# 알바생 강호, S4, 그리디
# 팁 = 원래 주려고 생각했던 돈 - (받은 등수 - 1)
# 팁의 최대값 구하기, 많이 주는 사람이 앞으로(?)
from sys import stdin


n = int(stdin.readline())
arr = []
for i in range(n):
    arr.append(int(stdin.readline()))

arr.sort(reverse=True)
res = 0
for i in range(n):
    tmp = arr[i] - i
    if tmp < 0:
        res += 0
    else:
        res += tmp

print(res)