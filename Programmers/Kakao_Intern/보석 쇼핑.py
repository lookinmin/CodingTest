def solution(gems):
    N = len(gems)
    answer = [0, N - 1]  # 가장 최대의 범위를 시작으로
    dis_gems = list(set(gems))  # 각 구분된 gem들의 개수
    dic = {}
    for gem in dis_gems:
        dic[gem] = 0

    dic[gems[0]] = 1

    start = 0
    end = 0

    while start < N and end < N:
        k = 0
        for gem in dis_gems:
            if dic[gem] != 0:
                k += 1

        if k < len(dis_gems):
            end += 1
            if end == N:
                break
            dic[gems[end]] += 1
        else:
            if (end - start + 1) < (answer[1] - answer[0] + 1):
                # 갱신
                answer = [start, end]
            dic[gems[start]] -= 1

            start += 1

    answer[0] += 1
    answer[1] += 1
    return answer


# 시간초과 남


def solution(gems):
    N = len(gems)
    answer = [0, N - 1]  # 가장 최대의 범위를 시작으로
    dis_gems = len(set(gems))  # 각 구분된 gem들의 개수
    dic = {gems[0]: 1, }

    start = 0
    end = 0

    while start < N and end < N:
        if len(dic) < dis_gems:
            end += 1
            if end == N:
                break
            dic[gems[end]] = dic.get(gems[end], 0) + 1
            # 없으니 새로운 걸 가져오는 거라서, get을 통해 default값을 0으로 해 새로운 gem을 가져옴
        else:
            if (end - start + 1) < (answer[1] - answer[0] + 1):
                # 갱신
                answer = [start, end]
            # 다 들어있는데 길이가 더 김
            if dic[gems[start]] == 1:  # 하나만 있음
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1

            start += 1

    answer[0] += 1
    answer[1] += 1
    return answer