# 콘센트, G5
from sys import stdin
import heapq
n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort(reverse=True)
conc = []

for num in arr:
    if len(conc) < m:
        heapq.heappush(conc, num)
    else:
        heapq.heappush(conc, num + heapq.heappop(conc))

print(max(conc))

