def solution(n, left, right):
    answer = []
    # row, col 중 큰 값의 + 1이 해당 index의 배열 값
    for i in range(left, right + 1):
        a = i // n
        b = i % n
        tmp = max(a, b)
        answer.append(tmp + 1)
    return answer