# 강의실, G5, 그리디-우선순위 큐
# 시작시간 기준 정렬

import heapq
from sys import stdin

n = int(stdin.readline().rstrip())

q =[]
# 강의 번호는 필요없을듯
for _ in range(n):
    a,b,c  = map(int,stdin.readline().split())
    q.append([b, c])

q.sort()

room = []
heapq.heappush(room, q[0][1])

for i in range(1, n):
    if q[i][0] < room[0]:       # 방 하나 더 필요
        heapq.heappush(room,q[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room,q[i][1])

print(len(room))