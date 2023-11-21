import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]

    for path in paths:
        graph[path[0]].append((path[1], path[2]))
        graph[path[1]].append((path[0], path[2]))

    is_summit = [False] * (n+1)

    for summit in summits:
        is_summit[summit] = True

    dist = [int(1e9)] * (n+1)
    q = []

    for gate in gates:
        dist[gate] = 0
        heapq.heappush(q, [0, gate])

    while q:
        distance, now = heapq.heappop(q)

        if dist[now] < distance or is_summit[now]:
            # 산봉우리거나, 갱신 불가능일때,
            continue

        for v, w in graph[now]:
            w = max(dist[now], w)
            if dist[v] > w:     # 최대 상태로 갱신
                dist[v] = w     # 아니면 갱신할 필요 없음
                heapq.heappush(q, ([w, v]))

    res = [-1, int(1e9)]

    for summit in sorted(summits):  # 산봉우리가 number가 작은거 먼저
        if dist[summit] < res[1]:
            res[1] = dist[summit]
            res[0] = summit

    return res


