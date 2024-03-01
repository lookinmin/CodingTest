# 블라인드, S4

from sys import stdin
m, n = map(int, stdin.readline().split())

k = 5 * m + 1
width = 5 * n + 1
window = [[] for _ in range(k)]

for i in range(k):
    window[i] = stdin.readline().rstrip()

x, y = 1, 1

def isWhat(x, y):
    cnt = 0
    for i in range(4):
        for j in range(4):
            if window[x + i][y + j] == '*':
                cnt += 1
    if cnt == 0:
        return 0
    elif cnt == 4:
        return 1
    elif cnt == 8:
        return 2
    elif cnt == 12:
        return 3
    else:
        return 4

res = [0] * 5
for i in range(0, k-5, 5):
    for j in range(0, width - 5, 5):
        res[isWhat(x + i, y + j)] += 1

print(*res)