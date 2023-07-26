# 숨바꼭질4, G4, BFS

from sys import stdin
from collections import deque

INF = 100000

n, k = map(int, stdin.readline().split())
graph = [0]*(INF+1)

cnt = 0
move = [0]*(INF+1)  # 이동 경로 들어갈 배열
                    # 각 인덱스의 값에는 이전에 방문한 노드가 들어간다

def path(x):        # 이동 경로 찾는 함수
    res = []
    tmp = x         # 마지막 방문 노드
    for _ in range(graph[x] + 1):
        res.append(tmp)     # 해당 노드를 res에 넣는다, res는 방문의 역순으로 들어감
        tmp = move[tmp]     # 마지막 방문 이전 노드
    return res

ans = []
def bfs(s):
    global cnt
    global ans

    q = deque()
    q.append(s)

    while q:
        x = q.popleft()
        if x == k:
            cnt = graph[x]
            ans = path(x)
            break

        for nx in (x-1, x+1, 2*x):
            if 0<=nx<=INF:
                if graph[nx] == 0 or graph[nx] == graph[x] + 1:
                    graph[nx] = graph[x] + 1
                    q.append(nx)
                    move[nx] = x


bfs(n)
print(cnt)
ans.reverse()
print(*ans)
