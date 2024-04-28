# 크리스마스 선물, S3
from sys import stdin
import heapq
n = int(stdin.readline())

heap = []
for _ in range(n):
    arr = list(map(int, stdin.readline().split()))
    if arr[0] == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(-1)
    else:
        for w in arr[1:]:
            heapq.heappush(heap, -w)