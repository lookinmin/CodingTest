def check(shop, discount):
    tmp = shop.copy()
    for t in discount:
        if t in tmp:
            if tmp[t] > 0:
                tmp[t] -= 1

    if sum(tmp.values()) == 0:
        return True

    return False


def solution(want, number, discount):
    answer = 0

    shop = {}
    for i in range(len(want)):
        shop[want[i]] = number[i]

    for j in range(len(discount) - 9):
        tmp = discount[j: j + 10]
        if check(shop, tmp):
            answer += 1

    return answer