from collections import deque
def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[0]*m for _ in range(n)]
    
    def bfs(a, b, rm):
        dx = [-1 ,1 ,0 ,0]
        dy = [0, 0, -1, 1]
        q = deque()
        q.append([a, b])
        visited[a][b] = rm
        
        cnt = 1
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                    if land[nx][ny] == 1:
                        q.append([nx, ny])
                        visited[nx][ny] = rm
                        cnt += 1
        return cnt;
    
    room_num = 1
    room_dic = dict()
    room_dic[0] = 0
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                room_dic[room_num] = bfs(i, j, room_num)
                room_num += 1
    
    res = 0
    
    for y in range(m):
        tmp = 0
        seen = set()
        for x in range(n):
            if visited[x][y] not in seen:
                seen.add(visited[x][y])
                tmp += room_dic[visited[x][y]]
        res = max(res, tmp)
    return res