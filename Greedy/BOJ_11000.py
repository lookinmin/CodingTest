# 강의실 배정, G5, 그리디 - 정렬
# s to t, n개의 수업, 강의실 최소화
# 시작 시간 기준 정렬
# 우선순위 큐
from sys import stdin
import heapq

n = int(stdin.readline())
q = []
for _ in range(n):
    s, t = map(int,stdin.readline().split())
    q.append([s,t])

q.sort()        # 시작 시간 기준 정렬

room = []
heapq.heappush(room, q[0][1])   # 첫번째 강의의 끝나는 시간을 큐에 담는다
# 다음 시작시간과의 비교를 통해
# 현재 room = [3]

for i in range(1, n):
    if q[i][0] < room[0]:       # 다음 회의 시작시간이 끝나는 시간보다 빠름
        heapq.heappush(room, q[i][1])    # 회의실 + 1
    else:
        heapq.heappop(room)     # 시간 변경 위해 pop
        heapq.heappush(room, q[i][1])       # 시간 변경 -> 가장 늦은걸로

print(len(room))