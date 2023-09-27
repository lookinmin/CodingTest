# 숨바꼭질2, G4, BFS

from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())

Max = 10**5

graph = [0] * (Max+1)

cnt = 0
res = 0

def bfs(n):
    global cnt
    global res
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        tmp = graph[x]
        if x == k:
            cnt = tmp
            res += 1
            continue
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= Max:
                if graph[nx] == 0 or graph[nx] == graph[x] + 1:
                    # 이미 한번 갔더라도 X+1과 동일하다면 같은 레벨로 볼 수 있다.
                    q.append(nx)
                    graph[nx] = graph[x] + 1


bfs(n)
print(cnt)
print(res)
