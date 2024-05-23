# 차집합, S4
from sys import stdin
n, m = map(int, stdin.readline().split())
a = set(map(int, stdin.readline().split()))
b = set(map(int, stdin.readline().split()))

tmp = a - b
print(len(tmp))
print(*sorted(list(tmp)))