from sys import stdin
from collections import deque
from itertools import combinations

n = int(stdin.readline())
people = [0] + list(map(int, stdin.readline().split()))

graph = [[] for _ in range(n + 1)]

for i in range(1, n+1):
    graph[i] = list(map(int, stdin.readline().split()))[1:]


def bfs(arr):
    q = deque()
    q.append(arr[0])
    visited[arr[0]] = 1

    count_people = people[arr[0]]

    while q:
        now = q.popleft()

        for node in graph[now]:
            if not visited[node] and node in arr:
                visited[node] = 1
                count_people += people[node]
                q.append(node)

    return count_people

cities = [i for i in range(1, n + 1)]
res = int(1e9)

for i in range(1, n // 2 + 1):
    for comb in combinations(cities, i):
        visited = [0] * (n + 1)
        arr1 = list(comb)
        arr2 = list(set(cities) - set(comb))    # 하나 구하고 남은 하나
        sum1 = bfs(arr1)
        sum2 = bfs(arr2)
        if 0 in visited[1:]:        # 하나라도 못돌음
            continue
        res = min(res, abs(sum1 - sum2))

if res == int(1e9):
    print(-1)
else:
    print(res)

