`# 올림픽, S5, 구현

from sys import stdin

n, k = map(int, stdin.readline().split())

medal = [list(map(int, stdin.readline().split())) for _ in range(n)]

medal = sorted(medal, key = lambda x : (x[1], x[2], x[3]), reverse=True)

idx = [medal[i][0] for i in range(n)].index(k)

for i in range(n):
    if medal[idx][1:] == medal[i][1:]:
        print(i + 1)
        break


`