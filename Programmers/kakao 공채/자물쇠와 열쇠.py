def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(e) for e in list_of_tuples]

def solution(key, lock):
    answer = True

    N = len(lock)
    M = len(key)

    new_lock = [[0] * (N * 3) for _ in range(N * 3)]

    for i in range(N):
        for j in range(N):
            new_lock[i + N][j + N] = lock[i][j]

    location = []
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                location.append([i, j])

    tmp = 0
    for line in key:
        tmp += line.count(1)

    if len(location) > tmp:
        return False
    elif len(location) == len(lock) ** 2:
        return True

    turn90 = rotated(key)
    turn180 = rotated(turn90)
    turn270 = rotated(turn180)

    keys = [key, turn90, turn180, turn270]

    def check(new_lock):
        for row in range(N, N * 2):
            for col in range(N, N * 2):
                if new_lock[row][col] != 1:
                    return False
        return True


    for i in range(4):
        now_key = keys[i]

        for x in range(N*2):
            for y in range(N*2):
                for i in range(M):
                    for j in range(M):
                        new_lock[x+i][y+j] += now_key[i][j]

                if check(new_lock):
                    return True

                for i in range(M):
                    for j in range(M):
                        new_lock[x + i][y + j] -= now_key[i][j]
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], 	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))