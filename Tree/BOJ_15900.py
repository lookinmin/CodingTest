# 나무 탈출, S1, 트리
# 한 노드의 여러 개 말 가능 -> BTree?
# 루트에 도착하면 말 제거
# 성원이가 선 -> 루트에서 리프까지 거리가 홀수면 승
# 모든 리프노드에 말 존재

from sys import stdin
import sys
sys.setrecursionlimit(10**5)

n = int(stdin.readline())
res = 0
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
distance = [0 for _ in range(n+1)]      # 해당 리프노드부터 루트까지의 거리를 담을 배열

for _ in range(n-1):
    a, b = map(int,stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            distance[i] = distance[v] + 1
            dfs(i)

dfs(1)

for i in range(2, n+1):         # 루트를 제하고 루트 바로 밑의 노드부터 탐색시작
    if len(graph[i]) == 1:      # 연결된게 하나밖에 없으니 리프노드
        res += distance[i]      # 총 거리의 합

if res %2 ==0:
    print("No")
else:
    print("Yes")
