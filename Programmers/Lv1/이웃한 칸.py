def solution(board, h, w):
    answer = 0

    pick = board[h][w]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]

        if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
            if board[nx][ny] == pick:
                answer += 1

    return answer