# 주차장
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
costs = deque()
cars = deque()
for _ in range(n):
    costs.append(int(stdin.readline()))
res = 0

cars.append(0)
for _ in range(m):
    cars.append(int(stdin.readline()))

wait = deque()
location = [0] * n

for i in range(2*m):
    now = int(stdin.readline())

    if now > 0:
        if 0 in location:
            for j in range(n):
                if location[j] == 0:
                    location[j] = now
                    break
        else:
            wait.append(now)
    else:
        car_num = location.index(-now)
        location[car_num] = 0
        res += cars[-now] * costs[car_num]
        if wait:
            location[car_num] = wait.popleft()

print(res)