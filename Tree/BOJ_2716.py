# 원숭이 매달기, S2
from sys import stdin
n = int(stdin.readline())

for _ in range(n):
    tree = stdin.readline().rstrip()
    stack = []
    maxDepth = 0

    for o in tree:
        if o == ']':
            maxDepth = max(len(stack), maxDepth)
            stack.pop()
        else:
            stack.append('[')

    print(2**maxDepth)