# 선발 명단, G5, 브루트 포스

from sys import stdin

T = int(stdin.readline())

def solve(col, total):
    global res, visited
    if col == 11:               # 11개의 행을 모두 탐색했다면(가로)
        res = max(res, total)
        return
    for i in range(11):
        if visited[i] == 1:
            continue
        if arr[col][i] == 0:
            continue
        total += arr[col][i]        # 현재 총합 값에 현재 값 넣어줌
        visited[i] = 1
        solve(col + 1, total)       # 한 칸 아래로 내리면서 탐색
        total -= arr[col][i]        # 총합 값 초기화
        visited[i] = 0              # 방문 초기화

for _ in range(T):
    arr = [[] for _ in range(11)]
    visited = [0] * 11              # 한 열에 대해 방문했다면 해당 열은 방문하지 않음

    for i in range(11):
        arr[i] = list(map(int, stdin.readline().split()))

    res = 0

    solve(0, 0)
    print(res)
