# S1, 태권왕
from sys import stdin
from collections import deque

t = int(input())

def bfs(start, end):
    q = deque()
    q.append((start, end, 0))
    visited = set([(start, end)])
    
    while q:
        now, target, dist = q.popleft()
        
        if now == target:
            return dist
        
        score1 = now * 2
        targetUpdate = target + 3
        
        if score1 <= targetUpdate and (score1, targetUpdate) not in visited:
            visited.add((score1, targetUpdate))
            q.append((score1, targetUpdate, dist + 1))
        
        score2 = now + 1
        if score2 <= target and (score2, target) not in visited:
            visited.add((score2, target))
            q.append((score2, target, dist + 1))
    return -1

for _ in range(t):
    me, you = map(int, stdin.readline().split())
    res = bfs(me, you)
    print(res)