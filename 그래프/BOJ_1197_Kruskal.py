from sys import stdin

v, e = map(int, stdin.readline().split())
edges = []
parent = [i for i in range(v + 1)]
depth = [0] * (v + 1)        # 각 정점의 depth

for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    edges.append((a, b, c))

def find(parent, x):        # 끝 조상 찾기
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, depth, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    
    if rootX != rootY:      # 현재 두 정점이 속한 사이클이 다르다면
        if depth[rootX] > depth[rootY]:     # depth가 더 낮은 트리를 높은 트리 밑으로
            parent[rootY] = rootX           # UNION
        elif depth[rootX] < depth[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX           # 두 트리의 높이가 같으면
            depth[rootX] += 1               # 합칠 때 깊이 + 1

def kruskal(edges):
    edges.sort(key = lambda x : x[2])
    # 가중치 기준 최소부터
    
    total_weight = 0
    edge_count = 0
    
    for edge in edges:
        a, b, weight = edge
        
        if find(parent, a) != find(parent, b):  # 사이클 없음
            union(parent, depth, a, b)
            total_weight += weight
            edge_count += 1
            
            if edge_count == v-1:
                break
    return total_weight

print(kruskal(edges))