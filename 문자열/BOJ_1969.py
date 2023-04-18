# DNA, S4, 문자열-구현
# A,T,G,C
# Hamming Distance = 같은 길이의 2 DNA에서 각 위치의 문제가 다른것의 개수
from sys import stdin

n, m = map(int, stdin.readline().split())
arr = []
for i in range(n):
    s = list(map(str, stdin.readline().rstrip()))
    arr.append(s)

res = ""
cnt = 0
ans = 0     # 수 합

for i in range(m):
    A,C,G,T = 0,0,0,0

    for j in range(n):
        if arr[j][i] == 'A':
            A += 1
        elif arr[j][i] == 'C':
            C += 1
        elif arr[j][i] == 'G':
            G += 1
        elif arr[j][i] == 'T':
            T += 1
    tmp = max(A,C,G,T)
    if tmp == A:
        res += 'A'
        ans += C + G + T
    elif tmp == C:
        res += 'C'
        ans += A + G + T
    elif tmp == G:
        res += 'G'
        ans += C + A + T
    elif tmp == T:
        res += 'T'
        ans += C + G + A
print(res)
print(ans)