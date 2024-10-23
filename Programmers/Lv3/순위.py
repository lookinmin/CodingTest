from collections import deque

def bfs(graph, s):
    visited = set()
    q = deque()
    q.append(s)
    
    cnt = 0
    visited.add(s)
    
    while q:
        v = q.popleft()
        for adj in graph[v]:
            if adj not in visited:
                visited.add(adj)
                q.append(adj)
                cnt+=1
    return cnt

def solution(n, results):
    lose = [[] for _ in range(n + 1)]
    win = [[] for _ in range(n + 1)]
    
    for a, b in results:
        win[a].append(b)
        lose[b].append(a)
    
    res = 0
    for node in range(1, n + 1):
        if (bfs(win, node) + bfs(lose, node)) == n - 1:
            res+=1
        
    return res