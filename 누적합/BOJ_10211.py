# Maximum Subarray, 실버4, 누적 합

from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    a.insert(0, 0)
    psum = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        psum[i] = psum[i-1] + a[i]
    # 최대 구간합 = max(psum[i] - psum[k])
    # == psum[i] - min(psum[k])
    minPrefix = 0
    sol = float('-inf')
    for i in range(1, n+1):
        tmp = psum[i] - minPrefix
        sol = max(tmp, sol)
        minPrefix = min(minPrefix, psum[i])

    print(sol)

