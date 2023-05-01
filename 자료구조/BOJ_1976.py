# 여행가자, G4, 그래프 탐색-UnionFind
# 순서대로 가능?

# union-find 알고리즘 문제
# 특정 v 부터 v'까지 이어져있는지 확인
# 여행계획이 하나의 집합에 속하면 YES

from sys import stdin
from collections import deque

n = int(stdin.readline())
m = int(stdin.readline())
parents = [i for i in range(n)]     # 노드들의 집합

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

def find(v):
    if v != parents[v]:             # 내 부모 노드가 내가 아닌 경우,
        parents[v] = find(parents[v])   # 부모노드를 찾아서 해당 번호의 노드에 부모노드로 저장
    return parents[v]               # 해당 노드의 부모노드 리턴

for i in range(n):
    tmp = list(map(int, stdin.readline().split()))
    for j in range(n):
        if tmp[j] == 1:
            union(i, j)     # 두 노드를 union

parents = [-1] + parents        # 0번째 노드는 없음
travel = list(map(int, stdin.readline().split()))
s = parents[travel[0]]      # 시작노드
for i in range(1, m):
    if parents[travel[i]] != s:     # 결국 여행 시작노드와 현재 방문 노드가 연결되어 있지 않으면
        print("NO")                 # 여행할 수 없음
        break
else:
    print("YES")



