def solution(price, money, count):
    tmp = 0
    for i in range(1, count + 1):
        tmp += price * i

    return 0 if money >= tmp else abs(money - tmp)
에