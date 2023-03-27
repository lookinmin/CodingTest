# 숨바꼭질 3, G5, 다익스트라

from sys import stdin
import heapq
from collections import deque

n ,k = map(int, stdin.readline().split())
INF = int(1e9)

graph = [0] * 100001

q= deque()
q.append(n)
graph[n] = 1

while q:
    x = q.popleft()
    if x == k:
        print(graph[k] - 1)
        break
    for i in (2*x, x-1, x+1):
        if 0 <= i <100001 and graph[i] == 0:
            if i == 2*x:
                graph[i] = graph[x]             # 0초니까 안 더함
                q.appendleft(i)                 # 여기가 핵심
            else:
                graph[i] = graph[x] + 1         # 1초니까 더함 + 1
                q.append(i)

