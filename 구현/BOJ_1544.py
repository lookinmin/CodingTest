# 사이클 단어, S4
from sys import stdin
from collections import deque

n = int(stdin.readline())
dic = set()
dic.add(stdin.readline().rstrip())
for _ in range(n - 1):
    arr = deque(stdin.readline().rstrip())
    for _ in range(len(arr)):
        tmp = ''.join(arr)
        if tmp in dic:
            break
        arr.rotate()
    else:
        dic.add(''.join(arr))
    
print(len(dic))