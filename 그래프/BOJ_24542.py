# S1, 튜터-튜티 관계의 수
from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1
    
    cnt = 0     # 각 시작 노드에 대해 시작 노드로부터 몇개의 노드가 연결되어 있는지 카운트
    
    while q:
        node = q.popleft()
        cnt += 1
        
        for v in graph[node]:
            if not visited[v]:
                visited[v] = 1
                q.append(v)
    return cnt      # 연결되어 있는 노드 수 리턴

visited = [0] * (n+1)

tree_size = []
for i in range(1, n + 1):
    if not visited[i]:      # 방문되지 않은 노드에 대해
        tree_size.append(bfs(i))       
        # 각 노드를 시작점으로 bfs 수행, 해당 노드에 연결된 노드 갯수로 comps 배열 생성


res = 1
for size in tree_size:  # 각 트리의 크기(연결된 노드의 수)          
    # 각 노드를 시작점으로 했을 때 연결되어있는 노드들의 수에 대해 곱 계산 수행
    res = (res * size) % 1000000007

print(res)