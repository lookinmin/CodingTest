def solution(a, b):
    answer = 0

    t = min(a, b)
    k = max(a, b)

    for i in range(t, k + 1):
        answer += i

    return answer