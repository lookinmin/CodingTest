# 강의실 배정, G5, 그리디

from sys import stdin
import heapq
n = int(stdin.readline())
arr = []
for _ in range(n):
    s, e = map(int, stdin.readline().split())
    arr.append([s,e])

arr.sort()

q = []
for start, end in arr:
    if q and start >= q[0]:     # q에 값이 존재하는지 여부 판별이 없었음
        heapq.heappop(q)
    heapq.heappush(q,end)

print(len(q))
