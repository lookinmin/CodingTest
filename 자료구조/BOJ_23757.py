# 아이들과 선물상자, S2
from sys import stdin
import heapq
n, m = map(int, stdin.readline().split())
boxes = list(map(int, stdin.readline().split()))
kids = list(map(int, stdin.readline().split()))
boxQ = []

for box in boxes:
    heapq.heappush(boxQ, -box)

for kid in kids:
    value = -heapq.heappop(boxQ)
    if value < kid:
        print(0)
        exit()
    value -= kid
    heapq.heappush(boxQ, -value)

print(1)
