# 미친로봇, G4
from collections import deque

lst = list(map(int, input().split()))
n = lst[0]

probability = [0.01 * i for i in lst[1:]]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]  # E W S N

start = (0, 0)
visited = set()
visited.add(start)


def dfs(x, y, cnt, prob):
    if cnt == 0:
        return prob
    
    total_prob = 0
    
    for i in range(4):
        if probability[i] == 0:
            continue
        nx, ny = x + dx[i], y + dy[i]
        if (nx,ny) not in visited:
            visited.add((nx, ny))
            total_prob += dfs(nx, ny, cnt - 1, prob * probability[i])
            visited.remove((nx, ny))
            
    return total_prob

res = dfs(0, 0, n, 1)
print(res)