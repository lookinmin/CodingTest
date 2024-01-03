from collections import deque
def solution(N, road, K):
    answer = 0

    # 시작은 1
    # 1-> 1은 0이 걸리니 무조건 받을 수 있다.
    # 즉, 고려할 필요가 없음
    graph = [[] for _ in range(N + 1)]

    INF = int(1e9)

    visited = [INF] * (N + 1)
    # 0 초기화 -> 시간초과
    # INF 초기화 -> 성공
    # 차이가 뭘까

    for a, b, c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])

    q = deque()
    q.append([1, 0])
    visited[1] = 1

    while q:
        node, weight = q.popleft()

        for v, w in graph[node]:
            if weight + w <= K and weight + w < visited[v]:     # 더 짧게 가는 방법이 있다면 이를 갱신한다.
                visited[v] = weight + w                         # 여기서 차이가 발생하는 듯
                q.append([v, weight + w])

    for v in visited:
        if v != INF:
            answer += 1

    return answer