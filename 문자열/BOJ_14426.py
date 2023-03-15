# 접두사 찾기, S1, 문자열-트리

from sys import stdin
n,m= map(int, stdin.readline().split())
s = []
for _ in range(n):
    s.append(stdin.readline().rstrip())

t = []
for _ in range(m):
    t.append(stdin.readline().rstrip())

s.sort()            # 시간 단축을 위해 정렬
t.sort()

cnt = 0
tmp = 0
for a in t:
    for i in range(tmp, n):
        if a == s[i][:len(a)]:
            cnt += 1
            tmp = i
            break
print(cnt)