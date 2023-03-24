# 다익스트라 간단한 구현

import sys
input = sys.stdin.readline
INF = int(1e9)          # 무한

n, m = map(int, input())        # n = 노드 개수 / m = edge 수
start = int(input())            # 시작 노드

graph = [[] for _ in range(n + 1)]
visited = [0] * (n+1)
distance = [INF] * (n+1)        # 거리 정보를 담을 리스트

for _ in range(m):
    a, b, c = map(int, input().split())     # a노드에서 b노드로 가는 weight = c
    graph[a].append((b,c))  # 노드 a에 (b,c) 형태로 append

def get_smallest():
    # not visited 노드 중, 가장 최단거리가 짧은 노드의 번호 반환
    min_value = INF
    idx = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = 1
    return idx

def dijkstra(start):
    distance[start] = 0
    visited[start] = 1

    for i in graph[start]:
        distance[i[0]] = i[1]       # edge에 해당 weight 부여

    for i in range(n-1):
        now = get_smallest()        # 현재 가장 weight가 낮은 노드에 대해
        visited[now] = 1            # 방문처리함

        for j in graph[now]:        # 현재 방문한 노드에 연결되어 있는 노드들에 대해
            cost = distance[now] + j[1]     # 현재노드를 거쳐 다른 노드로 이동하는 거리에 대해 확인
            if cost < distance[j[0]]:       # 더 짧다면
                distance[j[0]] = cost       # 리스트 최신화

    dijkstra(start)

    for i in range(1,n+1):
        if distance[i] == INF:
            print("INF")        # 도달 불가 (끊어졌거나)
        else:
            print(distance[i])