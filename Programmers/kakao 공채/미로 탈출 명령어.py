from collections import deque

def solution(n, m, x, y, r, c, k):
    dx = [1, 0, 0, -1]  # d l r u
    dy = [0, -1, 1, 0]  # 0 1 2 3
    direction = ['d', 'l', 'r', 'u']

    def Distance(x, y, r, c):
        return abs(r-x) + abs(c-y)

    def bfs():
        q= deque([])
        q.append([x, y, 0, ''])

        while q:
            a, b, cnt, s = q.pop()

            if a == r and b == c:
                if cnt == k:
                    return s
                elif (k-cnt) % 2 == 1:      # 2. impossible 조건 찾기
                    return "impossible"
            tmp = []

            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]

                if 0 < nx <= n and 0 < ny <= m and Distance(nx,ny, r, c) + cnt < k: # 갈 수 있음
                    tmp.append([nx, ny, cnt + 1, s + direction[i]])

            tmp.reverse()
            q += tmp
        return 'impossible'

    answer = bfs()
    return answer

#---------------------------------------------------- DFS 풀이
from collections import deque
import sys

sys.setrecursionlimit(10 ** 8)
answer = 'z'

def dfs(n, m, x, y, r, c, s, cnt, k):
    global answer

    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    direction = ['d', 'l', 'r', 'u']

    if cnt + abs(r - x) + abs(c - y) > k:
        return
    if x == r and y == c and cnt == k:
        answer = s
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 < nx <= n and 0 < ny <= m and s < answer:  # 문자열 비교...
            # 미쳤냐.. 이거 어캐 생각함 시발
            dfs(n, m, nx, ny, r, c, s + direction[i], cnt + 1, k)

def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c)
    if dist > k or (k - dist) % 2 != 0:
        return 'impossible'

    dfs(n, m, x, y, r, c, '', 0, k)

    return answer

