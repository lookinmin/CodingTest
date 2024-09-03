from sys import stdin
from collections import deque
from itertools import combinations

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    dist = [-1] * (n + 1)
    q = deque([start])
    dist[start] = 0
    
    while q:
        node = q.popleft()
        
        for v in graph[node]:
            if dist[v] == -1:
                dist[v] = dist[node] + 1
                q.append(v)
    return dist

res = []
nums = [i for i in range(1 ,n + 1)]
for comb in combinations(nums, 2):
    dist1 = bfs(comb[0])
    dist2 = bfs(comb[1])
    
    total = 0
    for i in range(1, n + 1):
        total += 2 * min(dist1[i], dist2[i])
    res.append([min(comb[0], comb[1]), max(comb[0], comb[1]), total])

res.sort(key=lambda x: (x[2], x[0], x[1]))

# 올바른 출력 형식으로 수정
print(res[0][0], res[0][1], res[0][2])
