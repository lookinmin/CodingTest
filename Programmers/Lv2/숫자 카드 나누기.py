import math
def solution(arrayA, arrayB):
    # 한쪽껀 다 나눌 수 있고, 즉 최대 공약수
    # 나머지 쪽과는 서로소

    res = 0
    gcdA = arrayA[0]
    gcdB = arrayB[0]

    for num in arrayA[1:]:
        gcdA = math.gcd(num, gcdA)

    for num in arrayB[1:]:
        gcdB = math.gcd(num, gcdB)

    flagA = True
    flagB = True

    for num in arrayA:
        if num % gcdB == 0:
            flagA = False
            break
    if flagA:
        res = max(res, gcdB)

    for num in arrayB:
        if num % gcdA == 0:
            flagB = False
            break
    if flagB:
        res = max(res, gcdA)
    return res
