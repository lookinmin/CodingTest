# 피보나치, S3, DP

from sys import stdin

T = int(stdin.readline())
fibo = [1, 1, 2]
for i in range(3, 10001):
    fibo.append(fibo[i-1] + fibo[i-2])

for x in range(1, T+1):
    p, q = map(int, stdin.readline().split())

    val = fibo[p-1]
    res = val % q
    print("Case #{}: {}".format(x, res))
    x += 1
