import math


def solution(left, right):
    answer = 0
    # 소수도 약수가 2개
    # n**2는 약수가 3개

    for i in range(left, right + 1):
        if math.ceil(i ** (0.5)) == int(i ** (0.5)):
            answer -= i
        else:
            answer += i
    return answer