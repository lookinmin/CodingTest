# 알파벳 블록, S2
from sys import stdin
from collections import deque
now = deque()
n = int(stdin.readline())
stack = []
for _ in range(n):
    op = list(map(str, stdin.readline().split()))
    if op[0] == '1':
        now.append(op[1])
        stack.append('back')
    elif op[0] == '2':
        now.appendleft(op[1])
        stack.append('front')
    else:
        if stack:
            value = stack.pop()
            if value == 'back':
                now.pop()
            else:
                now.popleft()

if len(now) == 0:
    print('0')
else:
    print("".join(now))
