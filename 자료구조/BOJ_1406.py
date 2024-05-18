# 에디터, S2
from sys import stdin

origin = list(stdin.readline().rstrip())
n = int(stdin.readline())
tmp = []

for _ in range(n):
    op = stdin.readline().split()
    if op[0] == 'L':
        if origin:
            tmp.append(origin.pop())
    elif op[0] == 'D':
        if tmp:
            origin.append(tmp.pop())
    elif op[0] == 'B':
        if origin:
            origin.pop()
    else:
        origin.append(op[1])
        
res = ''

print(''.join(origin + tmp[::-1]))