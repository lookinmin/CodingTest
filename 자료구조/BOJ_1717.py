# 집합의 표현, G5, 집합
from sys import stdin
import sys
sys.setrecursionlimit(10**7)

n, m = map(int, stdin.readline().split())
parent = [i for i in range(n + 1)]

def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    x, y = find(a), find(b)

    if x > y:
        parent[x] = y
    elif x < y:
        parent[y] = x


for _ in range(m):
    op, a, b = map(int, stdin.readline().split())
    if op == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")