# 나의 FIFA 팀 가치는?, S2
from sys import stdin
import heapq
from collections import defaultdict
# 3월 -> 8월 (all -1) -> 11월 (재구성)

n, k = map(int, stdin.readline().split())
team = defaultdict(list)

for _ in range(n):
    p, w = map(int, stdin.readline().split())
    heapq.heappush(team[p], -w)

while k > 0:
    k -= 1

    for i in range(1, 12):
        if len(team[i]) > 0:
            value = -heapq.heappop(team[i])
            if value > 0:
                value -= 1
            heapq.heappush(team[i], -value)

res = 0
for i in range(1, 12):
    if len(team[i]) > 0:
        res += -heapq.heappop(team[i])
    else:
        res += 0

print(res)
