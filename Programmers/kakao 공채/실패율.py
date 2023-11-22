def solution(N, stages):
    answer = []
    # 미클 / 일단 온사람
    game = [0] * (N + 1)  # 각 스테이지에 도달한 사람
    on = [0] * (N + 1)  # 각 스테이지 깬 사람

    for stage in stages:
        if stage == N + 1:
            for i in range(1, N + 1):
                game[i] += 1
                on[i] += 1
        else:
            for i in range(1, stage + 1):
                game[i] += 1
                on[i] += 1

    for idx in stages:
        if idx < N + 1:
            on[idx] -= 1
    res = {}
    for i in range(1, N + 1):
        if game[i] == 0:
            res[i] = 0
        elif on[i] == 0:
            res[i] = 1
        else:
            res[i] = ((game[i] - on[i]) / game[i])

    tmp = sorted(res.items(), key=lambda x: x[1], reverse=True)
    for i in tmp:
        answer.append(i[0])

    return answer

# 시간초과


def solution(N, stages):
    answer = []
    # 미클 / 일단 온사람
    sum_list = [0] * (N + 2)

    stages.sort()
    now = len(stages)

    for stage in stages:
        sum_list[stage] += 1

    res = {}
    for i in range(1, N + 1):
        if now == 0:
            res[i] = 0
            continue
        res[i] = sum_list[i] / now
        now -= sum_list[i]          # 이결 생각 못했네

    tmp = sorted(res.items(), key=lambda x: x[1], reverse=True)
    for i in tmp:
        answer.append(i[0])

    return answer

