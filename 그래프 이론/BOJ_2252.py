# 줄 세우기, G3, 위상 정렬

from sys import stdin
n, m = map(int, stdin.readline().split())

from collections import deque

graph = [[] for _ in range(n+1)]
inDegree = [0] * (n+1)

for i in range(m):
     a, b = map(int, stdin.readline().split())
     graph[a].append(b)
     inDegree[b] += 1


q = deque()         # 차수가 낮은 순대로 받아줄 큐 선언하고
res = []            # 결과 담을 배열

for i in range(1, n+1):
    if inDegree[i] == 0:        # 해당 노드의 차수가 0 이면
        q.append(i)             # q에 넣는다

while q:
    tmp = q.popleft()           # 차수가 0인 값들 중 q에 들어온 순서대로 빼주고       # 이거 heapq으로 하면 틀리나
    res.append(tmp)
    for i in graph[tmp]:        # 해당 노드와 연결된 노드들의
        inDegree[i] -= 1        # 차수를 하나씩 빼주고
        if inDegree[i] == 0:    # 노드의 차수가 0이면
            q.append(i)         # q에 append

print(*res)