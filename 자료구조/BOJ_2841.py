# 외계인의 기타 연주
from sys import stdin

n, p = map(int, stdin.readline().split())
res = 0
stack = [[] for _ in range(n + 1)]
for _ in range(n):
    line, prat = map(int, stdin.readline().split())

    if len(stack[line]) == 0:
        res += 1
        stack[line].append(prat)
    else:
        if stack[line][-1] == prat:
            continue
        elif stack[line][-1] < prat:
            res += 1
            stack[line].append(prat)
        else:
            while stack[line][-1] > prat:
                stack[line].pop()
                res += 1

                if len(stack[line]) == 0:
                    break

            if len(stack[line]) == 0:
                res += 1
                stack[line].append(prat)
            else:
                if stack[line][-1] == prat:
                    continue
                else:
                    stack[line].append(prat)
                    res += 1

print(res)

