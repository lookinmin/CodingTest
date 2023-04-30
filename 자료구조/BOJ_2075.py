# N번째 큰 수, S2, 우선순위 큐

from sys import stdin
import heapq

n = int(stdin.readline())
arr = []

for i in range(n):
    tmp = map(int, stdin.readline().split())
    for j in tmp:
        if len(arr) < n:        # 메모리 제한으로 인해 heapq의 크기를 5로 제한할 것
            heapq.heappush(arr, j)
        else:
            if arr[0] < j:
                heapq.heappop(arr)
                heapq.heappush(arr, j)
print(arr[0])

