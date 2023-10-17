# 문자열 폭발, G4, 문자열

from sys import stdin

s = stdin.readline().rstrip()
bomb = list(stdin.readline().rstrip())
k = len(bomb)
stack = []

for w in s:
    stack.append(w)

    if len(stack) >= k:
        u = -1*k
        tmp = stack[u:]
        if tmp == bomb:
            for i in range(k):
                stack.pop(-1)

if len(stack) == 0:
    print("FRULA")
else:
    for w in stack:
        print(''.join(w), end='')