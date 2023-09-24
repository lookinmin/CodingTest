# 최소 회의실 갯수, G5, 그리디

from sys import stdin
import heapq

n = int(stdin.readline())
arr = []

for _ in range(n):
    start, end = map(int, stdin.readline().split())
    arr.append([start, end])

arr.sort()
# 끝나는 시각만 heap에 push
q = []

for s, e in arr:
    if q and q[0] <= s:     # 이전 회의가 끝나고 다음 회의를 시작할 수 있음
        heapq.heappop(q)    # 이전 회의 제거(회의실 사용 완)
    heapq.heappush(q, e)    # 회의 시작 -> 끝 시간 push

print(len(q))


