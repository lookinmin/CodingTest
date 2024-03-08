# 수열과 쿼리 38, S3, 구현

from sys import stdin
m = int(stdin.readline())
xor = 0
tmp = 0
for _ in range(m):
    op = list(map(int, stdin.readline().split()))
    if op[0] == 1:
        xor ^= op[1]
        tmp += op[1]
    elif op[0] == 2:
        xor ^= op[1]
        tmp -= op[1]
    elif op[0] == 3:
        print(tmp)
    else:
        print(xor)