# 소-난다!, S2
from sys import stdin
import math

n, m = map(int, stdin.readline().split())
arr = sorted(list(map(int ,stdin.readline().split())))

visited = [0] * n
res = []
total = set()

def isPrime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

def dfs(depth):
    if depth == m:
        if isPrime(sum(res)) and sum(res) not in total:
            total.add(sum(res))
        return

    for i in range(n):
        if not visited[i]:
            res.append(arr[i])
            visited[i] = 1
            dfs(depth + 1)
            visited[i] = 0
            res.pop()

dfs(0)

if len(total) == 0:
    print("-1")
else:
    print(*sorted(list(total)))
