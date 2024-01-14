# 친구비, G4, 그래프

from sys import stdin
import sys

sys.setrecursionlimit(10**9)

n ,m ,k = map(int, stdin.readline().split())
money = list(map(int, stdin.readline().split()))
graph = [[] for _ in range(n)]
for _ in range(m):
    v, w = map(int, stdin.readline().split())
    graph[v-1].append(w-1)
    graph[w-1].append(v-1)

friends = [False] * n

def dfs(v, store):
    # 각 노드에 대해 노드와 연결된 모든 노드들을 리턴한다.
    friends[v] = True
    for node in graph[v]:
        if not friends[node]:
            store.append(node)
            dfs(node, store)
    return store

res = []
for i in range(n):
    if not friends[i]:
        linked = dfs(i, [i])
        tmp = int(1e9)

        for v in linked:      # 연결된 그래프 안에서 가장 싼 값을 찾는다
            tmp = min(tmp, money[v])

        res.append(tmp) # 해당 연결 그래프에서 사용되는 비용

if sum(res) <= k:
    print(sum(res))
else:
    print("Oh no")
