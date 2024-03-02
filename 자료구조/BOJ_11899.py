# 괄호 끼워넣기, S3

from sys import stdin

s = stdin.readline().rstrip()
stack = []
cnt = 0
for w in s:
    if w == '(':
        stack.append('(')
    else:
        if len(stack) > 0:
            stack.pop()
        else:
            cnt += 1

print(cnt + len(stack))