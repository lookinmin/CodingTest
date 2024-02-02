import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    k = n // 5
    o = n % 5
    print("++++ " * k + '|'*o)