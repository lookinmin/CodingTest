# 풍선 맞추기, G5, 그리디
from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

res = [0] * 1000001
for num in arr:

    if res[num] > 0:
        res[num] -= 1
        res[num - 1] += 1
    else:
        res[num - 1] += 1

print(sum(res))