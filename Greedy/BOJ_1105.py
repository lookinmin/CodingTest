# 팔, S1, 그리디

from sys import stdin

L, R = stdin.readline().split()
res = 0
if len(L) != len(R):
    print(0)
else:
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i]== '8':
                res += 1
        else:
            break
    print(res)
