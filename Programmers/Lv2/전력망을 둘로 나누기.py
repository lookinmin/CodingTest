from collections import deque
def solution(n, wires):
    answer = int(1e9)
    
    graph = [[] for _ in range(n + 1)]
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    
    def bfs(s, endPoint):
        visited = [0] * (n+1)
        visited[s] = 1
        q = deque()
        q.append(s)
        
        cnt = 1
        
        while q:
            x = q.popleft()
            
            for node in graph[x]:
                if node != endPoint:
                    if visited[node] == 0:
                        q.append(node)
                        visited[node] = 1
                        cnt += 1
        return cnt
                    
    
    for v in range(1, n + 1):
        for node in graph[v]:
            a = bfs(v, node)
            b = bfs(node, v)
            answer = min(answer, abs(a-b))
    
    return answer