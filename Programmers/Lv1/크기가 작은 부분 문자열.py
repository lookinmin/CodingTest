# 크기가 작은 부분 문자열, Lv1

def solution(t, p):
    answer = 0

    k = len(p)
    for i in range(0, len(t) - k + 1):
        tmp = t[i: i + k]
        if int(tmp) <= int(p):
            answer += 1
    return answer