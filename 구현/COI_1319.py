# coding test
from sys import stdin

n = int(stdin.readline().rstrip())
arr = []
res = 1
a = sum(list(map(int, stdin.readline().split())))

for _ in range(n-1):
    b = sum(list(map(int, stdin.readline().split())))
    if b > a:
        res += 1


print(res)
