# 컨베이어 벨트 위의 로봇, G5, 구현

from sys import stdin
from collections import deque

n,k = map(int, stdin.readline().split())
belt = deque(list(map(int, stdin.readline().split())))

res = 0

robot = deque([0] * n)

while 1:
    belt.rotate(1)  # 한칸 왼쪽으로 회전
    robot.rotate(1) # 로봇도
    robot[-1] = 0       # 로봇은 n에서 내림

    if sum(robot):      # 로봇 존재
        for i in range(n-2, -1, -1):    # 로봇이 내리기 전부터
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:        # 다음 칸에 로봇 없고, 다음 칸 내구도가 1이상 이면,
                robot[i+1], robot[i] = 1, 0     # 로봇 이동
                belt[i+1] -= 1      # 내구도 -1
        robot[-1] = 0       # 로봇 끝내서 내리니까 0
    if robot[0] == 0 and belt[0] >= 1:      # 시작점에 로봇 없고, 시작점 내구도 >= 1 이면
        robot[0] = 1    # 로봇 올림
        belt[0] -= 1
    res += 1

    if belt.count(0) >= k:
        break
print(res)



