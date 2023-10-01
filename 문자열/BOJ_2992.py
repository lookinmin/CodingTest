# 크면서 작은수, S3, 문자열 - 백트래킹

from sys import stdin
from itertools import permutations

# permutation 풀이

X = stdin.readline().rstrip()

tmp = list(permutations(X, len(X)))
tmp.sort()
for num in tmp:
    k = ""
    for i in range(len(num)):
        k = k + str(num[i])
    if int(k) > int(X):
        print(int(k))
        exit(0)

print(0)

# 백트래킹 풀이

# 최대 수가 999,999
num = ""
minNum = "999999"
visited = [0]*len(X)

def dfs(depth):
    global num
    global minNum

    if depth == len(X):
        if X < num < minNum:
            minNum = num    # 가장 작은수를 바꿔줌
        return

    for i in range(len(X)):
        if visited[i] == 1:
            continue
        visited[i] = 1
        num += X[i]
        dfs(depth + 1)
        visited[i] = 0
        num = num[:-1]

dfs(0)

if minNum == '999999':
    print(0)
else:
    print(minNum)