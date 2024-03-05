from itertools import combinations
from collections import deque
import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
result = []
result.append(arr[0])
result.append(arr[1])
arr.pop(0)
arr.pop(0)
q = deque(arr)

while q:
    result.append(q.popleft())
    for i in range(2,len(result)+1):
        com = list(combinations(result,i))
        for y in range(len(com)):
            if sum(com[y]) not in arr:
                result.pop()
                break
    if len(result)==n:
        break
print(result)