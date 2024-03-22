# 두 스티커, S3

from sys import stdin

h, w = map(int, stdin.readline().split())
n = int(stdin.readline())
sticker = []
for i in range(n):
    r, c = map(int, stdin.readline().split())
    sticker.append([r, c])

res = 0

for i in range(n-1):
    for j in range(i + 1, n):
        r1, c1 = sticker[i]
        r2, c2 = sticker[j]

        value = r1*c1 + r2*c2

        if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
            res = max(res, value)
        if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and r2 + c1 <= w):
            res = max(res, value)
        if (c1 + r2 <= h and max(c2, r1) <= w) or (max(c1, r2) <= h and c2 + r1 <= w):
            res = max(res, value)
        if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
            res = max(res, value)
print(res)


