# 트리의 기둥과 가지, G5, 트리
# 기가 노드는 루트 노드에서 순회를 시작했을 때, 처음으로 자식 노드가 2개 이상인 노드
# 기둥은 루트 노드에서부터 기가 노드
# 가지는 기가 노드에서부터 임의의 리프 노드
# 가지의 길이는 가지의 간선 길이의 합

from sys import stdin
import sys
sys.setrecursionlimit(10**9)

n, r = map(int, stdin.readline().split())
tree = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(n-1):
    a, b, d = map(int, stdin.readline().split())
    tree[a].append((b,d))
    tree[b].append((a,d))

giga = -1       # 기가노드의 위치
res1 = 0        # 기둥의 길이(루트 - 기가)
res2 = 0        # 가지의 길이
leaf_check = 0  # 기가노드가 존재하지 않을 때, 거리를 저장할 변수

def dfs(s, cnt):                        # 루트부터 시작해서 기가노드의 위치를 알고, 기가노드가 없다면 leaf까지의 거리를 저장
    global res1, giga, leaf_check
    visited[s] = 1
    check = []

    for v, w in tree[s]:
        if not visited[v]:
            check.append([v, w])
            leaf_check += w         # 모든 트리가 자식노드가 1개 -> 기가노드가 없음, 늘 leaf에 w 더해줌

    if len(check) >= 2:     # 자식 노드가 2개 이상 -> 기가 노드 시점
        res1 = cnt
        giga = s
        return
    else:
        if check:
            dfs(check[0][0], cnt + check[0][1])

def dfs2(s, cnt):               # 기가노드부터 시작해 자식노드까지 탐색하면서 제일 높은 가중치의 합 구하기
    global res2
    visited[s] = 1              # 기가 노드의 방문 처리

    for v, w in tree[s]:        # 기가노드로부터 연결된 노드들에 대해
        if not visited[v]:      # 방문하면서
            res2 = max(res2, cnt + w)       # 가중치를 더해 제일 큰 값 초기화
            dfs2(v, cnt + w)                # 해당 노드의 자식노드로 재귀적 dfs


dfs(r, 0)               # 시작은 루트
dfs2(giga, 0)           # 시작은 기가노드

if giga == -1:
    print(leaf_check, res2)
else:
    print(res1, res2)


