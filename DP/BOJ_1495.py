# 기타리스트, 실버1, DP
# 매번 곡 시작전, 볼륨을 바꿈
from sys import stdin
input = stdin.readline
# n = 곡 개수, s = 시작볼륨, m = 볼륨의 최대값
n,s,m = map(int,input().split())
v = list(map(int,input().split()))

d = [[0]*(m+1) for _ in range(n+1)]
# d[i][j] = i번째 곡을 j 볼륨으로 만들 수 있는지 (1 가능 / 0 불가능)
d[0][s] = 1     # 0번째 곡(start) s 볼륨 -> 가능

for i in range(1 ,n+1):
    for j in range(m+1):
        if d[i-1][j] != 0:  # 볼륨 조절 가능?
            if 0 <= j + v[i-1] <= m:
                d[i][j + v[i - 1]] = 1      # P + V[i]
            if 0 <= j - v[i-1] <= m:
                d[i][j - v[i - 1]] = 1      # P - V[i]
ans = -1
# 볼륨의 최대값을 출력하기 위해 내림차순으로 반복문 실행
for i in range(m, -1, -1):
    if d[n][i] == 1:  # 최대값 발견하면 중단
        ans = i
        break

print(ans)

