from sys import stdin
n = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
lst.sort()

val = lst[0] * lst[1]
valE = lst[-1] * lst[-2]
print(max(val, valE))