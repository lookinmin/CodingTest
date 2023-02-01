# 모든 순열, S3, 완탐-백트래킹

# permutations 풀이
from itertools import permutations
n = int(input())
arr = [i for i in range(1, n+1)]
for i in list(permutations(arr)):
    for j in i:
        print(j, end=' ')
    print()


# dfs를 이용한 백트래킹 풀이
arr2 = []
def dfs():
    if len(arr2) == n:
        print(*arr2)
        return
    for i in range(1, n+1):
        if i not in arr2:
            arr2.append(i)
            dfs()
            arr2.pop()
dfs()