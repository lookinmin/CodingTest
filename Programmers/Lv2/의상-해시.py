def solution(clothes):
    dic = {}
    for cloth in clothes:
        dic[cloth[1]] = dic.get(cloth[1], 0) + 1
        # 이렇게도 쓸 수 있구나

    res = 1

    for type in dic:
        res *= (dic[type] + 1)

    res -= 1

    return res