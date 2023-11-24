def solution(board, skills):
    answer = 0

    n = len(board)
    m = len(board[0])

    for skill in skills:
        type = skill[0]
        r1 = skill[1]
        c1 = skill[2]

        r2 = skill[3]
        c2 = skill[4]

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if type == 1:
                    board[i][j] -= skill[5]
                else:
                    board[i][j] += skill[5]

    for x in range(n):
        for y in range(m):
            if board[x][y] > 0:
                answer += 1


    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))

# 정확성 통과, 효율성 fail
# 250,000까지 있는 skills를 어떻게 처리할 것인가
# 2차원 배열의 누적합을 통해 해결


def solution(board, skills):
    answer = 0

    n = len(board)
    m = len(board[0])

    tmp = [[0] * (m+1) for _ in range(n+1)]
    # 누적합 배열

    for type, r1, c1, r2, c2, degree in skills:

        if type == 2:
            tmp[r1][c1] += degree
        else:
            tmp[r1][c1] -= degree

        if type == 2:
            tmp[r1][c2 + 1] -= degree
        else:
            tmp[r1][c2 + 1] += degree

        if type == 2:
            tmp[r2+1][c1] -= degree
        else:
            tmp[r2 + 1][c1] += degree

        if type == 2:
            tmp[r2+1][c2+1] += degree
        else:
            tmp[r2 + 1][c2 + 1] -= degree

    for i in range(n):
        for j in range(m):
            tmp[i][j + 1] += tmp[i][j]

    for i in range(n):
        for j in range(m):
            tmp[i + 1][j] += tmp[i][j]

    for i in range(n):
        for j in range(m):
            board[i][j] += tmp[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer

