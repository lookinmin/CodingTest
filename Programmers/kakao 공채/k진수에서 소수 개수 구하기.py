import string


def convert(num, base):
    tmp = string.digits + string.ascii_lowercase
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


# 진법변환 출처 : https://security-nanglam.tistory.com/508#google_vignette

def isprime(n):
    if n <= 1: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True


def solution(n, k):
    answer = 0

    # 1. n을 k진법의 소수로 변환하기
    trans = convert(n, k)
    if len(trans) == 0:
        return 0

    div = trans.split('0')

    if len(div) == 0:
        return 0

    res = []
    for i in range(len(div)):
        if div[i].isdigit():
            res.append(int(div[i]))

    if len(res) == 0:
        return 0

    res.sort()

    # 2. 해당 수를 소수인지 판별
    for num in res:
        if isprime(num):
            answer += 1

    return answer