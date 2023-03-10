# 토지
from sys import stdin

arr = []
for _ in range(5):
    arr.append(list(map(int, stdin.readline().split())))

res = 0
for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
            res = abs(2-i) + abs(2-j)

print(res)