# 피자굽기, G5
from sys import stdin
D, N = map(int, stdin.readline().split())

oven = list(map(int, stdin.readline().split()))
pizza = list(map(int, stdin.readline().split()))

# 1. 오븐 재정의

for i in range(1, D):
    oven[i] = min(oven[i], oven[i-1])

# 5 6 4 3 6 2 3 -> 5 5 4 3 3 2 2

# 2. 반죽 넣기, 밑에서 부터
idx = 0

for i in range(D-1, -1, -1):
    if pizza[idx] <= oven[i]:
        idx += 1        # 못넣을 때 까지
    if idx == N:
        print(i + 1)
        break

if idx != N:
    print(0)

