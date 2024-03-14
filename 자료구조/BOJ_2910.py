# 빈도 정렬, S3
from sys import stdin

n, c = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

tmp = dict()

for num in arr:
    tmp[num] = tmp.get(num, 0) + 1

res = sorted(tmp.items(), key = lambda x : x[1], reverse=True)

for i in range(len(res)):
    for j in range(res[i][1]):
        print(res[i][0], end = " ")