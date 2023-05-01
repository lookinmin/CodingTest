# 거북이, S3, 구현
# F: 한 눈금 앞으로
# B: 한 눈금 뒤로
# L: 왼쪽으로 90도 회전
# R: 오른쪽으로 90도 회전


from sys import stdin

T = int(stdin.readline())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(T):
    moves = list(stdin.readline().rstrip())
    x, y = 0, 0
    direction = 0       # 0 북 1 서 2 남 3 동

    min_x, min_y, max_x, max_y = 0,0,0,0

    for move in moves:
        if move == 'F':         # 현재 방향으로 진행
            x = x + dx[direction]
            y = y + dy[direction]
        elif move == 'B':       # 현재 방향의 뒤로
            x = x - dx[direction]
            y = y - dy[direction]
        elif move == 'L':       # 현재 방향의 왼쪽으로 변경
            if direction == 3:  # 기존 방향이 동쪽
                direction = 0   # 왼쪽으로 돌리면 0
            else:
                direction += 1  # 나머진 왼쪽으로 돌림
        else:
            if direction == 0:  # 기존 방향이 북쪽
                direction = 3   # 오른쪽으로 돌리면 3
            else:
                direction -= 1
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    print(abs(max_x - min_x) * abs(max_y - min_y))