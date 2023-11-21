def solution(k, tangerine):
    answer = 0
    # 각 귤의 갯수를 센다
    gull = {}

    for g in tangerine:
        if g in gull:
            gull[g] += 1
        else:
            gull[g] = 1

    # 제일 많은 종류를 넣는다

    tmp = sorted(gull.items(), key=lambda x: x[1], reverse=True)
    cnt = 0
    i = 0
    while k > 0:
        cnt += 1
        k -= tmp[i][1]
        i += 1
    answer = cnt
    return answer