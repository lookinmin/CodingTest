# 방탈출, S2
from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

lights = [0] * n

res = 0

for i in range(n):
    if arr[i] != lights[i]:
        res += 1
        if i <= n - 3:
            for j in range(i, i + 3):
                if lights[j] == 1:
                    lights[j] = 0
                else:
                    lights[j] = 1
        elif i == n - 2:
            for j in range(i, i + 2):
                if lights[j] == 1:
                    lights[j] = 0
                else:
                    lights[j] = 1
        elif i == n - 1:
            for j in range(i, i + 1):
                if lights[j] == 1:
                    lights[j] = 0
                else:
                    lights[j] = 1

print(res)