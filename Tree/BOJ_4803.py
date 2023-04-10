# 트리, G4, 트리
# 사이클을 만드는 지 여부를 판단

from sys import stdin

def findCycle(s):
    for i in graph[s]:      # 찾는 노드에 대해 인접한 노드들 방문
        if parent[s] == i:      # 인접 노드가 자신의 부모노드인 경우 pass
            continue

        if visited[i]:      # 인접 노드가 방문처리 되었다는것
            return True     # 사이클릭인 경우

        parent[i] = s
        visited[i] = 1

        if findCycle(i):
            return True

    return False
case = 1
while 1:

    n, m = map(int, stdin.readline().split())
    if n == m == 0:
        break
    graph = [[] for _ in range(n+1)]
    parent = [-1] * (n+1)       # 각 노드에 대해 해당 노드의 부모노드를 저장할 리스트
    visited = [0] * (n+1)

    cnt = 0     # 사이클 갯수 세기

    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n+1):
        if visited[i] == 0:
            parent[i] = i
            visited[i] = 1

            if not findCycle(i):
                cnt += 1            # 트리 수 증가

    if cnt == 0:
        print("Case {}: No trees.".format(case))
    elif cnt == 1:
        print("Case {}: There is one tree.".format(case))
    else:
        print("Case {}: A forest of {} trees.".format(case, cnt))
    case += 1