# bfs
from collections import deque
def solution(x, y, n):
    dist = [0 for _ in range(y + 1)]
    q = deque()
    q.append(x)

    if x == y:
        return 0
    while q:
        nx = q.popleft()
        for i in range(3):
            if i == 0:
                cur = nx * 2
            if i == 1:
                cur = nx * 3
            if i == 2:
                cur = nx + n
            if cur > y or dist[cur]:
                continue

            if cur == y:
                return dist[nx] + 1
            q.append(cur)
            dist[cur] = dist[nx] + 1
    return -1

# ------------------------------------ SET
# set
def solution(x, y, n):
    answer = 0
    s = set()
    s.add(x)

    while s:
        if y in s:
            return answer

        nxt = set()
        for i in s:
            if i + n <= y:
                nxt.add(i + n)
            if i * 2 <= y:
                nxt.add(i * 2)
            if i * 3 <= y:
                nxt.add(i * 3)

        s = nxt
        answer += 1
    return -1