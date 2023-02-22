# 트리의 부모 찾기, S2, 트리
import sys
from sys import stdin
sys.setrecursionlimit(10**9)

n = int(stdin.readline())
tree = [[]for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(v):
    for i in tree[v]:
        if parent[i] == 0:      # 해당 노드의 부모가 없으면
            parent[i] = v       # 시작값->현재값을 부모로 설정 후 dfs
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(parent[i])