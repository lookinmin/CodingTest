# 케빈 베이컨의 6단계 법칙, S1, BFS
from sys import stdin
from collections import deque

n,m = map(int,stdin.readline().split())
graph=[[] for _ in range(n+1)]


for _ in range(m):
    a,b=map(int,stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]

def bfs(v):
    visited = [0] * (n + 1)         # 방문했는지 초기화를 여기서 해야됨
    q = deque([v])
    visited[v] = 1
    num = [0] * (n+1)
    while q:
        c = q.popleft()
        for i in graph[c]:
            if visited[i] == 0:
                visited[i] = 1
                num[i] = num[c] + 1
                q.append(i)
    return sum(num)

res = []

for i in range(1, n+1):
    res.append(bfs(i))

print(res.index(min(res)) + 1)