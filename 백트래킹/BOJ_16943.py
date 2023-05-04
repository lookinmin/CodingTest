# 숫자 재배치, S1, 조합-백트래킹

from sys import stdin
from itertools import permutations

a, b= map(str, stdin.readline().split())
res = []
for i in permutations(a):
    res.append(''.join(i))      # tuple의 값들을 분리하여 배열의 값으로 넣기
c = -1
for i in res:
    if i[0] == '0':
        continue
    i = int(i)
    if i < int(b):
        c = max(c, i)

print(c)