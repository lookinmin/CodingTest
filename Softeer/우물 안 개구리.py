from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
weight = [0] + list(map(int, stdin.readline().split()))
graph = [[] for _ in range(n + 1)]
cant = set()

for i in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(s):
    flag = True
    for v in graph[s]:
        if weight[v] > weight[s]:
            cant.add(s)
            flag = False
            break
        elif weight[v] < weight[s]:
            cant.add(v)
            continue
        elif weight[v] == weight[s]:
            flag = False
            cant.add(v)
            cant.add(s)
            break
    return flag
                
res = 0

for node in range(1, n + 1):
    if len(graph[node]) == 0:
        res += 1
        continue
    else:
        if node not in cant:
            if bfs(node):
                res += 1
print(res)