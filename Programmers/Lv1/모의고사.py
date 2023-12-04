# 1번 : 12345 12345
# 2번 : 21232425
# 3번 : 33 11 22 44 55

def solution(answers):
    answer = []

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    k = len(answers)

    one = one * k
    two = two * k
    three = three * k

    dic = {1: 0, 2: 0, 3: 0}
    for i in range(k):
        if answers[i] == one[i]:
            dic[1] += 1
        if answers[i] == two[i]:
            dic[2] += 1
        if answers[i] == three[i]:
            dic[3] += 1

    tmp = max(list(dic.values()))

    res = []
    for i in list(dic.keys()):
        if dic[i] == tmp:
            res.append(i)

    res.sort()
    return res

print(solution([1,3,2,4,2]))