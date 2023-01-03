# 한 줄로 서기, 실버2, 구현 ,그리디
from sys import stdin
n = int(stdin.readline())
a = list(map(int,stdin.readline().split()))
ans = [0 for i in range(n)]
for i in range(1, n+1):
    tmp = a[i-1]
    cnt = 0
    for j in range(n):
        if cnt == tmp and ans[j] == 0:          # 내가 현재 남은 사람 중, 제일 작은 사람
            ans[j] = i
            break
        elif ans[j] == 0:
            cnt += 1

print(*ans)