import heapq
def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n+1)]

    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))


    # 출발은 s
    # 도착은 a랑 b

    # 다익스트라?

    def dijkstra(start, end):
        INF = int(1e9)
        dist = [INF] * (n+1)

        q = []

        heapq.heappush(q, (0, start))
        dist[start] = 0

        while q:
            distance, now = heapq.heappop(q)

            if distance > dist[now]:
                continue
            for v, w in graph[now]:
                cost = w + distance
                if cost < dist[v]:
                    dist[v] = cost
                    heapq.heappush(q, (cost, v))
        return dist[end]

    res = []
    # 경유지 들린 다익스트라 구하기
    # ** 중요
    # s -> p + (p -> a && p -> b)

    for p in range(1, n+1):
        if p != s:
            s_to_p = dijkstra(s, p)
            p_to_a = dijkstra(p, a)
            p_to_b = dijkstra(p, b)
            tmp = s_to_p + p_to_a + p_to_b
            res.append(tmp)
        else:
            res.append(dijkstra(s, a) + dijkstra(s, b))

    answer = min(res)


    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
