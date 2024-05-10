# 카드 놓기, S3
from sys import stdin
from collections import deque

n = int(stdin.readline())
cards = [i for i in range(n, 0, -1)]
skills = list(map(int, stdin.readline().split()))[::-1]

res = deque()

for i in range(n):
    if skills[i] == 1:
        res.appendleft(cards.pop())
    elif skills[i] == 2:
        tmp = res.popleft()
        res.appendleft(cards.pop())
        res.appendleft(tmp)
    else:
        res.append(cards.pop())
        
print(*res)
