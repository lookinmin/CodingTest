# 배열 돌리기 3, G5, 구현

from sys import stdin

n, m, r = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

cal = list(map(int, stdin.readline().split()))
# 1 = 상하 반전
# 2 = 좌우 반전
# 3 = 오른쪽으로 90도
# 4 = 왼쪽으로 90도
# 5 = 배열을 크기가 N/2×M/2인 4개의 부분 배열
# 1 -> 2 / 2->3 ...
# 6 = 1 -> 4 / 4 -> 3 / 3 -> 2 ...

def one():
    tmp = [[0] * m for _ in range(n)]
    for i in range(n):
        tmp[i] = graph[n-1-i]

    return tmp

def two():
    tmp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            tmp[i][j] = graph[i][m-1-j]

    return tmp

def three(graph, n, m):
    # 90도 회전 알고리즘
    # 회전 후의 행 번호 = 회전 전의 열 번호
    # 회전 후의 열 번호 = N - 1 - 회전 전의 행 번호

    tmp = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            tmp[j][n-1-i] = graph[i][j]     # 이거 암기
    return tmp

def four(graph, n, m):
    tmp = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            tmp[m-j-1][i] = graph[i][j]

    return tmp

def five():
    tmp = [[0] * m for _ in range(n)]

    for i in range(n // 2):     # 1->2
        for j in range(m // 2):
            tmp[i][j + m // 2] = graph[i][j]

    for i in range(n // 2):     # 2->3
        for j in range(m//2, m):
            tmp[i + n // 2][j] = graph[i][j]

    for i in range(n//2, n):       # 3 -> 4
        for j in range(m//2, m):
            tmp[i][j - m//2] = graph[i][j]

    for i in range(n//2 , n):       # 4 -> 1
        for j in range(m//2):
            tmp[i - n // 2][j] = graph[i][j]

    return tmp

def six():
    tmp = [[0] * m for _ in range(n)]

    for i in range(n // 2):         # 1 -> 4
        for j in range(m//2):
            tmp[i + n//2][j] = graph[i][j]

    for i in range(n//2):           # 2 -> 1
        for j in range(m//2, m):
            tmp[i][j - m//2] = graph[i][j]

    for i in range(n//2 , n):       # 3 -> 2
        for j in range(m//2, m):
            tmp[i - n // 2][j] = graph[i][j]

    for i in range(n//2, n):        # 4 -> 3
        for j in range(m//2):
            tmp[i][j + m//2] = graph[i][j]

    return tmp

for num in cal:
    if num == 1:
        graph = one()
    elif num == 2:
        graph = two()
    elif num == 3:
        graph = three(graph, n, m)
        n, m = m, n     # 가로 세로 길이가 변함
    elif num == 4:
        graph = four(graph, n, m)
        n, m = m, n
    elif num == 5:
        graph = five()
    elif num == 6:
        graph = six()
for i in range(n):
    print(*graph[i])



