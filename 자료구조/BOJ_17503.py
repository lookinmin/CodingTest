# 맥주 축제, S1
import heapq
from sys import stdin

# 선호도, 도수 레벨
# 도수 레벨 > 간 레벨 -> 기절
# N개의 선호도 합 >= M
# 간 레벨의 최솟값 구하기

n, m, k = map(int, stdin.readline().split())
beers = [list(map(int, input().split())) for _ in range(k)]
beers.sort(key = lambda x : (x[1], x[0]))

q = []
now = 0
for pref, danger in beers:
    now += pref
    heapq.heappush(q, pref)

    if len(q) == n:
        if now >= m:
            res = danger
            break
        else:
            now -= heapq.heappop(q)

else:
    print(-1)
    exit()

print(res)
