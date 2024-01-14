def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    # weight 기준 오름차순 정렬
    # 알아서 낮은거 부터 들어감

    connect = set([costs[0][0]])
    # 간선 연결 정보

    while len(connect) != n:
        for cost in costs:
            v, w = cost[0], cost[1]
            weigth = cost[2]

            if v in connect and w in connect:
                continue
            if v in connect or w in connect:
                connect.update([cost[0], cost[1]])
                answer += weigth
                break
    # 딱 푸는게 그리디인데 그래프다?
    # Kruskal MST
    return answer