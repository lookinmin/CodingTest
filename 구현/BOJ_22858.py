# 원상복구, S3, 구현
from sys import stdin

N, K = map(int, stdin.readline().split())
end = list(map(int, stdin.readline().split()))
rule = list(map(int, stdin.readline().split()))

start = end

for _ in range(K):
    tmp = [0] * N

    for i in range(N):
        tmp[rule[i] - 1] = start[i]
    start = tmp
print(*start)