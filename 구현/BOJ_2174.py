# 로봇 시뮬레이션, G5, 구현-시뮬레이션

from sys import stdin

a, b = map(int, stdin.readline().split())
n, m = map(int ,stdin.readline().split())

robot = []
command = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]      # 북, 동, 남, 서

for i in range(n):
    x, y, dir = map(str, stdin.readline().split())
    if dir == 'N':
        dir = 0
    elif dir == 'E':
        dir = 1
    elif dir == 'S':
        dir = 2
    elif dir == 'W':
        dir = 3
    robot.append([int(x), int(y), dir])



for i in range(m):
    r, move, repeat = map(str, stdin.readline().split())
    command.append([int(r), move, int(repeat)])

for r, move, repeat in command:
    for _ in range(repeat):
        if move == 'F':
            dir = robot[r-1][2]

            robot[r-1][0] += dx[dir]        # 가로 방향 한칸 이동
            robot[r-1][1] += dy[dir]        # 세로 방향 한칸 이동

            if robot[r-1][0] > a or robot[r-1][1] > b or robot[r-1][0] <= 0 or robot[r-1][1] <= 0:
                print("Robot {} crashes into the wall".format(r))
                exit(0)
            # 다른 로봇이랑 부딪히는 지

            for j in range(n):
                if j != r-1:
                    if robot[r-1][0] == robot[j][0] and robot[r-1][1] == robot[j][1]:
                        print("Robot {} crashes into robot {}".format(r, j+1))
                        exit(0)

        elif move == 'L':
            robot[r-1][2] = (robot[r-1][2] - 1) %4
        elif move == 'R':
            robot[r - 1][2] = (robot[r - 1][2] + 1) % 4

print('OK')