import string


def convert(num, base):
    tmp = string.digits + string.ascii_lowercase
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(n, t, m, p):
    answer = ''
    num = 0
    turn = 1

    if m == p:
        p = 0

    while 1:
        trans = convert(num, n)
        for i in trans:
            now = turn % m
            if now == p:
                if i.isalpha():
                    i = i.upper()
                answer += i
                turn += 1
                if len(answer) == t:
                    break
            else:
                turn += 1
        num += 1

        if len(answer) == t:
            break

    return answer
