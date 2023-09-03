# 이모티콘, G4, 그래프

from sys import stdin
from collections import deque

# 1. 이모티콘 모두 복사 -> 저장
# 2. 모든 이모티콘 붙여넣기
# 3. 이모티콘 중 하나 삭제

n = int(stdin.readline())
dist = [[-1] * (n+1) for _ in range(n+1)]
q = deque()
q.append((1, 0))        # 화면 이모티콘 수, 클립보드 이모티콘 수
dist[1][0] = 0          # 화면에 1개, 클립보드에 0개 일 때, 0초 소요

while q:
    window, clip = q.popleft()
    if dist[window][window] == -1:      # 화면의 이모티콘을 모두 복사해 클립보드에 저장
        dist[window][window] = dist[window][clip] + 1       # 작업에 1초 걸림
        q.append((window, window))      # 화면 이모티콘 수를 클립보드에 저장

    if window + clip <= n and dist[window+clip][clip] == -1:    #  클립보드의 모든 이모티콘을 화면에 붙여넣기
        dist[window+clip][clip] = dist[window][clip] + 1
        q.append((window+clip, clip))   # 화면에 클립보드에 있던 이모티콘 수 추가

    if window - 1 >= 0 and dist[window-1][clip] == -1:      # 화면의 이모티콘 중 하나 제거
        dist[window-1][clip] = dist[window][clip] + 1
        q.append((window-1, clip))      # 화면에 이모티콘 하나 삭제

res = -1
for i in range(n+1):
    if dist[n][i] != -1:
        if res == -1 or res > dist[n][i]:
            res = dist[n][i]

print(res)


