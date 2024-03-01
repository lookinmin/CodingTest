from sys import stdin
from itertools import combinations

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

res = [arr[0], arr[1]]

if n == 2:
    print(*arr[0 : 2])
    exit(0)

tmp = arr[2:]

for num in tmp:
    if num == 1:
        res.append(num)
    else:
        break

while 1:


