def solution(a, b, n):
    answer = 0
    while n >= a:
        get = (n // a) * b
        rest = n % a
        answer += get
        n = get + rest

    return answer