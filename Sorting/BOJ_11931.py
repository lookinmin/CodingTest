# 수 정렬하기, S5
from sys import stdin
import heapq
n = int(stdin.readline())
arr = [0] * n
for i in range(n):
    arr[i] = int(stdin.readline().rstrip())

def heap_sort(arr):
    q = []
    for num in arr:
        heapq.heappush(q, -num)
    return [-heapq.heappop(q) for _ in range(len(arr))]

arr = heap_sort(arr)
for i in range(n):
    print(arr[i])

