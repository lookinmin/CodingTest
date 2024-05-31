# 폴짝폴짝, S2
from sys import stdin
from collections import deque

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
a, b = map(int, stdin.readline().split())
visited = [-1] * n

def bfs(start, end):
    q = deque([start])
    visited[start] = 0
    
    while q:
        node = q.popleft()
        
        for nx in range(node, n, arr[node]):
            if visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[node] + 1
                if nx == end:
                    return visited[nx]
        
        for nx in range(node, -1, -arr[node]):
            if visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[node] + 1
                if nx == end:
                    return visited[nx]    
    return -1

print(bfs(a-1, b-1))