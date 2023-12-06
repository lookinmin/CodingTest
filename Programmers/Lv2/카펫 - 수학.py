# 수학 풀이 - 정답

def solution(brown, yellow):
    answer = []
    # 가로 >= 세로
    total = brown + yellow

    for b in range(1, total + 1):
        if (total / b) % 1 == 0:  # 약수임
            a = total / b
            if a >= b:
                if 2 * a + 2 * b - 4 == brown:
                    return [a, b]

# 완탐으로 풀면 틀림


# 완탐 풀이 - 시간초과

def solution(brown, yellow):
    answer = []
    # 가로 >= 세로
    tmp = []
    for i in range(yellow, 0, -1):
        for j in range(1, i + 1):
            if i * j == yellow:
                tmp.append([i, j])
    print(tmp)

    if len(tmp) == 1:
        answer = [tmp[0][0] + 2, tmp[0][1] + 2]
        return answer

    for square in tmp:
        rec = (square[0] + 2) * (square[1] + 2) - (square[0] * square[1])
        if rec == brown:
            answer = [square[0] + 2, square[1] + 2]
            return answer
