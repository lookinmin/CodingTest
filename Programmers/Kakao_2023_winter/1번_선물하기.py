def solution(friends, gifts):
    answer = 0
    n = len(friends)
    # 1. 선물지수 딕셔너리
    present_rate = {}
    # 2. 이번달에 주고받은 선물 딕셔너리
    give_present = [[0] * n for _ in range(n)]

    friends.sort()

    # 각 이름을 숫자로 매핑
    cvt_num = {}
    for i in range(n):
        cvt_num[friends[i]] = i
        present_rate[i] = [0, 0]

    for gift in gifts:
        A = gift.split(' ')[0]  # 준사람
        B = gift.split(' ')[1]  # 받은사람
        present_rate[cvt_num[A]][0] += 1
        present_rate[cvt_num[B]][1] += 1

        give_present[cvt_num[A]][cvt_num[B]] += 1  # A가 주고 B가 받았다

    get_present = {}

    for i in range(n):
        for j in range(n):

            if i == j:
                continue

            if give_present[i][j] > give_present[j][i]:  # i가j한테 준게 많다
                if i in get_present.keys():
                    get_present[i] += 1  # i가 하나를 받는다
                else:
                    get_present[i] = 1
            elif give_present[i][j] < give_present[j][i]:  # i가j한테 받은게 많다
                if j in get_present.keys():
                    get_present[j] += 1  # j가 하나를 받는다
                else:
                    get_present[j] = 1
            else:
                rateA = (present_rate[i][0] - present_rate[i][1])
                rateB = (present_rate[j][0] - present_rate[j][1])

                if rateA > rateB:
                    if i in get_present.keys():
                        get_present[i] += 1
                    else:
                        get_present[i] = 1
                elif rateB > rateA:
                    if j in get_present.keys():
                        get_present[j] += 1
                    else:
                        get_present[j] = 1

    for i in get_present.keys():
        get_present[i] //= 2
    tmp = get_present.values()
    if len(tmp) > 0:
        answer = max(tmp)
    else:
        answer = 0
    return answer