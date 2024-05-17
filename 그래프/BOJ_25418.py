# 정수 a를 k로 만들기, S3
from sys import stdin
from collections import deque

a, k = map(int, stdin.readline().split())
# +1, x2
visited = [0] * 1000001
res = int(1e9)
def bfs(start):
    global res
    q = deque()
    q.append([start, 0])
    visited[start] = 1
    while q:
        x, cnt = q.popleft()
        
        if x == k:
            res = min(res, cnt)
            return
        
        for num in (x + 1, x*2):
            if 0<=num<=1000000 and not visited[num]:
                q.append([num, cnt + 1])
                visited[num] = 1

bfs(a)
print(res)