from sys import stdin

n, m = map(int, stdin.readline().split())
limit = [0] * 100
play = [0] * 100

s = 0
for _ in range(n):
    length, speed = map(int, stdin.readline().split())
    limit[s : s + length] = [speed] * length
    s += length

c = 0
for _ in range(m):
    l, sp = map(int, stdin.readline().split())
    play[c : c + l] = [sp] * l
    c += l

res = -1

for i in range(100):
    res = max(res, play[i] - limit[i])

print(res if res > -1 else 0)
