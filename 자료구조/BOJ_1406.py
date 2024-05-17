# 에디터, S2
from sys import stdin
from collections import deque

origin = deque(stdin.readline().rstrip())
n = int(stdin.readline())
tmp = deque()
for _ in range(n):
    op = list(stdin.readline().split())
    if op[0] == 'L':
        if origin:
            tmp.appendleft(origin.pop())
    elif op[0] == 'D':
        if tmp:
            origin.append(tmp.popleft())
    elif op[0] == 'B':
        if origin:
            origin.pop()
    else:
        origin.append(op[1])
        
res = ''

for w in origin:
    res += w
for w in tmp:
    res += w

print(res)