# 문제집, G2, 우선순위 큐

# 위상 정렬 = non cyclic, undirected DAG 에서 순서가 정해져 있는 작업을 수행
# 순서를 정해주는 알고리즘

# 위상 정렬 과정
# 1. 진입 차수가 0인 접점을 q에 append
# 2. q에서 pop() -> 해당 원소와 연결된 간선 제거
# 3. 제거한 후, 진입차수가 0인 정점 q에 append
# 4. 반복

# 주의 = cyclic graph는 위상 정렬을 할 수 없음

from sys import stdin
import heapq

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
inDegree = [0] * (n+1)      # 각 값들의 차수

q = []
for i in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)      # 그래프를 통해 연결해주고
    inDegree[b] += 1        # 더 늦게 풀어야되는 문제의 차수를 올려줌

for i in range(1, n+1):
    if inDegree[i] == 0:        # 각 값들에 대해 차수가 0이면(바로 풀어도 됨)
        heapq.heappush(q, i)    # 최소 힙을 통해 push
res = []
while q:
    x = heapq.heappop(q)        # 넣은 값들에 대해 작은거 부터 (차수가 0인 값)
    res.append(x)               # 순서대로 res에 넣어주고

    for i in graph[x]:          # 해당 값과 연결된 다른 값들에 대해
        inDegree[i] -= 1        # 차수를 하나씩 빼주고
        if inDegree[i] == 0:    # 차수가 0이라면
            heapq.heappush(q, i)        # 최소 힙을 통해 push

print(*res)

