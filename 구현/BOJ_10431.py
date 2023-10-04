# 줄 세우기, S5, 구현

from sys import stdin

P = int(stdin.readline())
for _ in range(P):
    tmp = list(map(int, stdin.readline().split()))
    T = tmp[0]
    arr = tmp[1:]
    res = 0

    for i in range(19):
        for j in range(i + 1, 20):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                res += 1
    print(T, res)