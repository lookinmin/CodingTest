# 센티와 마법의 뽕망치, S1, 구현

from sys import stdin
import heapq

n, h, t = map(int, stdin.readline().split())
origin = t
giants = []

for _ in range(n):
    tmp = int(stdin.readline().rstrip())
    if tmp >= h:
        heapq.heappush(giants, tmp)

while t>0:
    if len(giants) > 0:
        k = heapq.heappop(giants)
        if k > 1:
            k = k//2
        if k >= h:
            heapq.heappush(giants, k)
        t -= 1
    else:
        break

if len(giants) > 0:
    print("NO")
    print(max(giants))
else:
    print("YES")
    print(origin - t)

# --------------------------- 틀린 이유 : 최대 힙을 사용하여 풀어야 하는데 최소 힙을 사용함

n, h, t = map(int, stdin.readline().split())
cnt = 0

giants = []
for _ in range(n):
    tmp = int(stdin.readline().rstrip())
    heapq.heappush(giants,-tmp)         # 최대힙이니까 음수로 만들어서 입력

for i in range(t):      # 가능한 만큼
    k = heapq.heappop(giants)
    if abs(k) < h:          # 키가 작아졌으면 push하고 break
        heapq.heappush(giants, k)
    elif abs(k) == 1:
        heapq.heappush(giants, k)
    else:                   # 아직도 키가 더 크다면
        k = -(abs(k)//2)            # 다시 넣어야되니까 음수로 다시
        heapq.heappush(giants, k)
        cnt += 1

res = abs(min(giants))       # 현재 남은 거인들 중 가장 키가 큰 사람(음수니까)

if res < h:
    print("YES")
    print(cnt)
else:
    print("NO")
    print(abs(heapq.heappop(giants)))