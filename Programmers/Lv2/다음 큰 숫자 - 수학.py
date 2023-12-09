def solution(n):
    answer = 0

    k = bin(n)[2:].count('1')

    while 1:
        n += 1
        tmp = bin(n)[2:].count('1')
        if tmp == k:
            answer = n
            break

    return answer