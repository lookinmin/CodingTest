def solution(cap, n, deliveries, pickups):
    answer = 0
    # 먼데부터
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    deli = 0
    pick = 0

    for i in range(n):
        deli += deliveries[i]
        pick += pickups[i]
        # 둘다 0이면 방문할 필요 없음

        while deli > 0 or pick > 0:
            deli -= cap
            pick -= cap
            answer += (n-i) * 2

    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))