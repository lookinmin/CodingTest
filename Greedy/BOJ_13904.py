# 과제, G3, 그리디
# 하루에 과제 하나 가능

from sys import stdin
import heapq
# 과제 점수로 우선순위큐
# 마감일 기준, 마감일 많이 남은거부터 값 비교해서 가져오기

n = int(stdin.readline())
q = []
res = [0] * 1001

for i in range(n):
    d, w = map(int, stdin.readline().split())
    q.append([-w,d,w])        # 최대우선순위큐를 위해 -w 먼저 저장

heapq.heapify(q)

while q:
    tmp = heapq.heappop(q)
    for i in range(tmp[1], 0, -1):      # 해당 날짜부터
        if res[i] == 0:         # 해당 날짜에 점수 비어있으면
            res[i] = tmp[2]     # 해당 날짜에 점수 삽입
            break

print(sum(res))