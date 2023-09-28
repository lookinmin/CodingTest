# 창고 다각형, S2, 구현-완탐

from sys import stdin

n = int(stdin.readline())

arr = [0] * 1001
heightIdx = 0
height = 0
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    arr[x] = y

    if y > height:
        heightIdx = x
        height = max(y, height)

now = 0
res = 0

for i in range(heightIdx + 1):      # 가장 왼쪽부터 가장 높은 기둥까지
    now = max(arr[i], now)
    res += now

now = 0

for i in range(1000, heightIdx, -1):
    now = max(arr[i], now)
    res += now

print(res)