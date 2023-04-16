# 마인크래프트, S2, 구현
# 블록 제거 - 2초
# 블록 쌓기  - 1초

from sys import stdin
from collections import Counter

n,m,b = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

time = int(1e9)
height = 0

for i in range(257):
    use = 0     # 쌓은 블록
    take = 0    # 가져온 블록
    # use와 take + b 비교

    for x in range(n):
         for y in range(m):
             if graph[x][y] > i:        # 현재 기준은 i(0->1->2...)
                 take += graph[x][y] - i        # 기준 값보다 현재 칸의 블록이 더 많다면
                                                # 블록에서 기준값 만큼 빼준다
             else:
                 use += i - graph[x][y]
    if use > take + b:
        continue
    cnt = take * 2 + use        # 제거에 2초, 쌓는데 1초
    if cnt <= time:
        time = cnt
        height = i

print(time, height)
