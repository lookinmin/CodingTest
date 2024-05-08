# S3, 조합
import math
n, m = map(int, input().split())
print(math.comb(n, m))

def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

print(fact(n)//fact(n-m) * fact(m))