def solution(n):
    answer = 0
    if int(n ** 0.5) == n ** 0.5:
        return (n ** 0.5 + 1) ** 2

    return -1
