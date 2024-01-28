def solution(n):
    word = ['수', '박'] * 10000
    answer = ''
    i = 0
    while n > 0:
        answer += word[i]
        n -= 1
        i += 1

    return answer