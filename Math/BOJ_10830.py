# 행렬제곱, G4, 수학
from sys import stdin

n, b = map(int, stdin.readline().split())
matrix =[[] for _ in range(n)]

for i in range(n):
    matrix[i] = list(map(int, stdin.readline().split()))

# (0,0)*(0,0) + (0,1)*(1,0)         (0,0)*(0,1) + (0,1)*(1,1)
# (1,0)*(0,0) + (1,1)*(1,0)         (1,0)*(0,1) + (1,1)*(1,1)

def mul(U, V):
    k = len(U)
    Z = [[0] * k for _ in range(k)]

    for r in range(k):
        for c in range(k):
            tmp = 0
            for i in range(k):
                tmp += U[r][i] * V[i][c]
            Z[r][c] = tmp % 1000

    return Z



def square(matrix, b):
    if b == 1:
        for x in range(len(matrix)):
            for y in range(len(matrix)):
                matrix[x][y] %= 1000
        return matrix

    tmp = square(matrix, b//2)      # 분할정복
    if b%2 == 1:
        return mul(mul(tmp, tmp), matrix)
    else:
        return mul(tmp, tmp)

res = square(matrix, b)
for row in res:
    print(*row)