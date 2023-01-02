# 생일, 실버5, 구현-문자열

from sys import stdin

n = int(stdin.readline())
a = []
for i in range(n):
    x = list(stdin.readline().split())
    a.append(x)
a.sort(key= lambda c : (int(c[3]), int(c[2]), int(c[1])))

print(a[n-1][0])
print(a[0][0])