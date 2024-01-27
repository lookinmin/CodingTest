def solution(n):
    answer = []
    arr = [[0] * n for _ in range(n)]

    x = -1
    y = 0
    num = 1

    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:  # 아래
                x += 1
            elif i % 3 == 1:  # 오른쪽 ->
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            arr[x][y] = num
            num += 1

    for row in arr:
        for idx in row:
            if idx:
                answer.append(idx)
    return answer