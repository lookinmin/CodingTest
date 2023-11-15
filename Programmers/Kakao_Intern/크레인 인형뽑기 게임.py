def solution(board, moves):
    answer = 0
    k = len(board)  # 어차피 정사각형임

    stack = []
    for num in moves:
        t = num - 1
        top = -1
        for i in range(k):
            if board[i][t] != 0:
                top = board[i][t]
                board[i][t] = 0

            if top != -1:
                if len(stack) != 0:
                    if top == stack[-1]:
                        stack.pop()
                        answer += 2
                        break
                    else:
                        stack.append(top)
                        break
                else:
                    stack.append(top)
                    break

    return answer