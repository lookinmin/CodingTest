# 배열 탈출, G5, 최단거리-dp+다익스트라

from sys import stdin
import heapq

# 1,1 -> n,n까지 가는 최단 경로
# 1. 1≤i,j<n, 상수는 A[i][j+1] 또는 A[i+1][j]로만 건너갑니다.
# 2. i=n,1≤j<n, A[i][j+1]로만 건너갑니다.
# 3. 1≤i<n,j=n, A[i+1][j]로만 건너갑니다.
# 4. i=j=n, 경우 바로 출구로 갑니다.
# A[a][b]에서 A[c][d]로 건너가려면 A[a][b]>A[c][d]를 만족
# 버튼을 누르면 해당 원소의 값이 1 증가
# 버튼을 한 번 누르는 데에는 1원의 비용이 듭니다. 상수는 돈을 가능한 한 적게 들이면서 배열을 탈출

n = int(stdin.readline())
graph = [[] for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int,stdin.readline().split()))

for r in range(n):
    for c in range(n):
        if r-1 < 0 and c-1 < 0:
            continue
        prev_r, prev_c = int(1e9), int(1e9)

        if 0<=r-1:
            prev_r = dp[r-1][c] + (0 if graph[r][c] < graph[r-1][c] else graph[r][c] - graph[r-1][c] + 1)
        if 0<=c-1:
            prev_c = dp[r][c-1] + (0 if graph[r][c] < graph[r][c-1] else graph[r][c] - graph[r][c-1] + 1)

        dp[r][c] = min(prev_r, prev_c)

print(dp[n-1][n-1])