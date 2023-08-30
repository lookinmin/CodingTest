# 순회강연, G3, 그리디

from sys import stdin
import heapq

n = int(stdin.readline())

arr = []
for _ in range(n):
    arr.append(list(map(int, stdin.readline().split())))
    # arr[0] = p, arr[1] = d

arr.sort(key= lambda x : x[1])

heap = []
for p, d in arr:
    heapq.heappush(heap, p)
    if len(heap) > d:
        heapq.heappop(heap)

print(sum(heap))
