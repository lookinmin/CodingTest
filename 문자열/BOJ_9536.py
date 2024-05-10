# 여우는 어떻게 울지?, S3
from sys import stdin
from copy import deepcopy
t = int(stdin.readline())

for _ in range(t):
    total = list(map(str, stdin.readline().split()))
    while 1:
        tmp = stdin.readline().rstrip()
        if tmp == "what does the fox say?":
            print(*total)
            break
        else:
            now = tmp.split()[2]
            strcmp = deepcopy(total)
            for w in total:
                if w == now:
                    strcmp.remove(w)
            total = strcmp
