import math
def solution(n, stations, w):
    answer = 0
    # 전파가 전달안되는 구간의 길이를 리스트에 add
    # w 범위로 나눈다

    dist = []

    for i in range(1, len(stations)):
        dist.append((stations[i] - w - 1) - (stations[i - 1] + w))
        # 전파가 닿지 않는 거리 저장

    dist.append(stations[0] - w - 1)
    dist.append(n - (stations[-1] + w))

    for num in dist:
        if num <= 0:
            continue
        answer += math.ceil(num / ((w * 2) + 1))

    return answer