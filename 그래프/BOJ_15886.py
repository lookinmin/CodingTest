# 내 선물을 받아줘2, S3

from sys import stdin

n = int(stdin.readline())
road = stdin.readline().rstrip()

res = 0

for i in range(n - 1):
    if road[i : i +2] == 'EW':
        res += 1

print(res)