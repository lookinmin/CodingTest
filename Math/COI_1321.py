# upgrade

from sys import stdin
n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
i = 1
while 1:
    if i not in arr:
        print(i)
        break
    i += 1