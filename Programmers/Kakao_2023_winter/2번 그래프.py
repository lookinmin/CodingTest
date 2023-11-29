def solution(edges):
    answer = []

    maxE = max(max(edges))

    graph = [[] for _ in range(maxE + 1)]

    for edge in edges:
        graph[edge[0]].append(edge[1])

    tmp = []
    for v in range(1, maxE + 1):
        if len(graph[v]) > 1:
           tmp.append(v)

    for v in range(1, maxE + 1):
        for node in graph[v]:
            if node in tmp:
                tmp.remove(node)

    new_node = tmp[0]
    answer.append(new_node)

    # 2. 새로 생긴 노드 지우기

    graph[new_node] = []

    visited = [0] * (maxE + 1)
    isCycle = [0] * (maxE + 1)

    donut, bar, eight = 0, 0, 0

    def dfs(s):
        visited[s] = 1
        cnt = 0
        isCycle[s] = 1

        for v in graph[s]:
            if visited[v] == 0:
                cnt += dfs(v)
            elif isCycle[v] == 1:
                cnt += 1
        isCycle[s] = 0
        return cnt



    can_bar = []
    for i in range(1, maxE + 1):
        if i == new_node:
            continue
        if i in graph[i] and len(graph[i]) == 1:       # [1,1] 경우
            donut += 1
            continue
        if len(graph[i]) == 0:
            can_bar.append(i)
            continue
        if visited[i] == 0:
            cnt = dfs(i)
            if cnt == 0:
                bar += 1
            elif cnt == 1:
                donut += 1
            else:
                eight += 1

    for i in can_bar:
        if visited[i] == 0:
            bar += 1

    answer.append(donut)
    answer.append(bar)
    answer.append(eight)



    # 출처 : https://sosoeasy.tistory.com/35
    # 그래프내의 Cycle여부 판단

    # 출처 : https://velog.io/@since-1994/%EA%B7%B8%EB%9E%98%ED%94%84-Detection-cycle-%EC%82%AC%EC%9D%B4%ED%81%B4-%EC%B0%BE%EA%B8%B0
    # 그래프내의 Cycle여부 판단

    return answer

print(solution(

[[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))