# 네트워크 연결, G4, 그래프 - MST
# MST : 트리의 일종, uncyclic graph
# 정점이 n개 = n-1개의 edge
# 구현 알고리즘 = prim or kruskal

# kruskal 알고리즘으로 해결해보기 - 그리디
# 1. 그래프 간선들 가중치를 오름차순으로 정렬
# 2. 정렬된 edge 리스트에서 사이클을 형성하지 않는 edge 선택 -> 가장 낮은 weight edge 선택
# 3. 2번 반복 -> 간선의 수가 정점-1 되었을 때 종료
# https://chanhuiseok.github.io/posts/algo-33/

from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
parent = [0] * (n+1)    # 부모 테이블 초기화
edges = []          # 모든 edge가 들어올 리스트
res = 0

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())        # 방향이 있음
    edges.append((a,b,c))

edges.sort(key = lambda x : x[2])       # edge weight 순 정렬

def find(x):        # 특정 원소가 속한 집합 찾기
    if parent[x] != x:          # 루트 노드까지 재귀적 호출
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):            # 두 원소가 속한 집합 합치기
    pa = find(a)             # 현재 노드에 대한 루트 노드
    pb = find(b)

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

for edge in edges:
    a,b,cost = edge

    if find(a) != find(b):      # 사이클이 발생하지 않음 ? 루트 노드가 다르니까
        union(a,b)
        res += cost

print(res)
