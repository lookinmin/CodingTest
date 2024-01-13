def solution(park, routes):
    n = len(park)
    m = len(park[0])
    x = 0
    y = 0
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                x = i
                y = j
                break

    dir = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

    for route in routes:
        op, go = route.split(' ')

        dx, dy = x, y
        # 현 위치

        for i in range(int(go)):
            nx = x + dir[op][0]
            ny = y + dir[op][1]

            if 0 <= nx < n and 0 <= ny < m and park[nx][ny] != 'X':
                x, y = nx, ny
            else:
                x, y = dx, dy
                break

    return (x, y)