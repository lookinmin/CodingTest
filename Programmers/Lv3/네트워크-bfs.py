from collections import deque

def solution(n, computers):
    answer = 0
    # 연결된 그래프의 갯수 구하기

    # 인접행렬로 표현된 그래프

    graph = [[] for _ in range(n)]
    visited = [0] * n

    for i in range(n):
        for j in range(n):
            if i != j:
                if computers[i][j] == 1:
                    graph[i].append(j)

    def bfs(s):
        q = deque()
        q.append(s)
        visited[s] = 1

        while q:
            node = q.popleft()
            for v in graph[node]:
                if visited[v] == 0:
                    q.append(v)
                    visited[v] = 1

    for node in range(n):
        if visited[node] == 0:
            bfs(node)
            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

# ----------------------------------------


from collections import deque

def solution(n, computers):
    graph = [set() for _ in range(n)]
    visited = [0] * n
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].add(j)
                graph[j].add(i)
    
    def bfs(node):
        q = deque()
        visited[node] = 1
        q.append(node)
        
        while q:
            v = q.popleft()
            
            for adj in graph[v]:
                if not visited[adj]:
                    visited[adj] = 1
                    q.append(adj)
        return
    
    res = 0
    for num in range(n):
        if not visited[num]:
            res+=1
            bfs(num)
    
    return res