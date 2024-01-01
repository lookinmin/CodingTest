def solution(d, budget):
    answer = 0
    # 부서의 수가 최대가 되야함
    d.sort()

    for val in d:
        tmp = budget - val
        if tmp >= 0:
            budget -= val
            answer += 1
        else:
            break

    return answer