def solution(begin, end):
    answer = []
    # 각 칸의 번호 중 최대값의 약수
    # 해당 칸의 값은 제외

    for i in range(begin, end + 1):
        min_num, max_num = 1, 1
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                if i // j <= 10000000:
                    min_num = j
                    answer.append(i // j)
                    break
                else:
                    max_num = j
        if i == 1:
            answer.append(0)
        elif min_num == 1:
            answer.append(max_num)
    return answer