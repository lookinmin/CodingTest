def solution(dirs):
    answer = 0

    dx = [0, 0, 1, -1]  # U D R L
    dy = [1, -1, 0, 0]

    x, y = 0, 0

    road = []

    for w in dirs:
        if w == 'U':
            nx, ny = x + dx[0], y + dy[0]
        elif w == 'D':
            nx, ny = x + dx[1], y + dy[1]
        elif w == 'R':
            nx, ny = x + dx[2], y + dy[2]
        elif w == 'L':
            nx, ny = x + dx[3], y + dy[3]

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            px = x
            py = y
            x = nx
            y = ny
            if [px, x, py, y] not in road and [x, px, y, py] not in road:
                road.append([px, x, py, y])
        else:
            nx = x
            ny = y

    return len(road)