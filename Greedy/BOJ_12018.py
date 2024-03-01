# Yonsei TOTO, S3, 그리디

from sys import stdin

n, m = map(int, stdin.readline().split())
res = 0
total = []

for _ in range(n):
    p ,l = map(int, stdin.readline().split())
    points = sorted(list(map(int, stdin.readline().split())), reverse=True)

    if p < l:
        total.append(1)
    else:
        total.append(points[l -  1])

total.sort()
for num in total:
    if m - num >= 0:
        m -= num
        res += 1

print(res)