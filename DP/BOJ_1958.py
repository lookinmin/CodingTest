# LCS3, G3, DP-문자열
# LCS 찾기
from sys import stdin
a = str(stdin.readline().strip())
b = str(stdin.readline().strip())
c = str(stdin.readline().strip())

x = len(a)
y = len(b)
z = len(c)
arr = [[[0] * (z+1) for _ in range(y+1)]for _ in range(x+1)]

for i in range(1, x+1):
    for j in range(1, y+1):
        for k in range(1, z+1):
            if a[i-1] == b[j-1] == c[k-1]:
                arr[i][j][k] = arr[i-1][j-1][k-1] + 1
            else:
                arr[i][j][k] = max(arr[i-1][j][k], arr[i][j-1][k], arr[i][j][k-1])

res = -1
for i in range(x + 1):
    for j in range(y + 1):
        res = max(max(arr[i][j]), res)

print(res)