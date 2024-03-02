# 4연산, G5, 그래프
# s->t
from sys import stdin
from collections import deque
s, t = map(int, stdin.readline().split())

op = ['*', '+', '/']

if s == t:
    print(0)
    exit(0)

INF = int(1e9)

def bfs():
    q = deque()
    q.append((s, ''))
    visited = set()

    res = -1

    while q:
        now, ex = q.popleft()
        if now == t:
            res = ex
            break

        for i in range(3):
            nx = eval("{}{}{}".format(now, op[i], now))
            if 0<=now<=INF and nx not in visited:
                q.append((nx, ex + op[i]))
                visited.add(nx)

    return res

print(bfs())