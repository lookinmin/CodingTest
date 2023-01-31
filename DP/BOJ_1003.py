# 피보나치 함수, S3, DP

from sys import stdin
T = int(stdin.readline())

def fib(n):
    zero = [1,0,1]
    one = [0, 1, 1]
    if n >= 3:
        for i in range(2, n):
            zero.append(zero[i-1] + zero[i])
            one.append(one[i-1] + one[i])
    print("{} {}".format(zero[n], one[n]))


for _ in range(T):
    n = int(stdin.readline())
    fib(n)