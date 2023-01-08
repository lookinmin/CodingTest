# 카드 합체 놀이, 그리디, 실버 1
from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

for i in range(m):
    arr.sort()
    arr[0] = arr[1] =  arr[0] + arr[1]

print(sum(arr))

# 여기 까지 O(nlogn)의 풀이

# O(logn) 풀이 = heap 사용
import heapq
res = []
for i in arr:
    heapq.heappush(res, i)      # 힙에 push       # == heapq.heapify(arr) 힙으로 만든다

for i in range(m):
    card1 = heapq.heappop(res)
    card2 = heapq.heappop(res)
    heapq.heappush(res, card1 + card2)
    heapq.heappush(res, card1 + card2)

print(sum(res))