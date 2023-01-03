# 문자열, 실버4, 문자열-브루트 포스

from sys import stdin
a, b = stdin.readline().split()

ans = []
for i in range(len(b)- len(a) + 1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1
    ans.append(cnt)

print(min(ans))

