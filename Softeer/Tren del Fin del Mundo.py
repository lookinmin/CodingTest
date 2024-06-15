from sys import stdin
n = int(input())
rails = []
for _ in range(n):
    x, y = map(int, input().split())
    rails.append([x, y])

rails.sort(key = lambda x : x[1])
print(*rails[0])