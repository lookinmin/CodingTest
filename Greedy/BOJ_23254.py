# 나는 기말고사형 인간이야, G5
from sys import stdin
import heapq
n, m = map(int, stdin.readline().split())
# 총 공부 시간
time = n * 24
scores = list(map(int, stdin.readline().split()))
upgrade = list(map(int, stdin.readline().split()))

res = 0
heap = []

for idx in range(m):
    heapq.heappush(heap, [-upgrade[idx], idx])

while heap:
    plus, idx = heapq.heappop(heap)
    plus = -plus

    x = (100 - scores[idx]) // plus
    if (100 - scores[idx]) % plus:
        heapq.heappush(heap, [-(100 - scores[idx] - x * plus), idx])
    if x >= time:
        x = time
    scores[idx] += plus * x
    time -= x
    if time == 0:
        break

print(sum(scores))