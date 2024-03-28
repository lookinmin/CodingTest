# 마니또, S1
from sys import stdin
from collections import deque

num = 1
while 1:
    n = int(stdin.readline())
    if n == 0:
        break
    graph = dict()
    for i in range(n):
        a, b = map(str, stdin.readline().split())
        graph[a]=b

    chain = dict()

    for name in graph.keys():
        chain[name] = 0

    cnt = 1
    def bfs(start):
        global cnt
        q = deque()
        q.append(start)
        chain[start] = cnt

        while q:
            now = q.popleft()
            nxt = graph[now]
            if chain[nxt] == 0:
                chain[nxt] = cnt
                q.append(nxt)
        return

    for name in graph.keys():
        if chain[name] == 0:
            bfs(name)
            cnt += 1

    print("{} {}".format(num, len(set(chain.values()))))

    num += 1