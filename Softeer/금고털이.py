from sys import stdin

w, n = map(int, stdin.readline().split())
jewels = []
for i in range(n):
    M, P = map(int, stdin.readline().split())
    jewels.append([P, M])

sorted_jewels = sorted(jewels, key = lambda x : (-x[0]))

res = 0

for v, m in sorted_jewels:
    if m <= w:
        res += (v * m)
        w -= m
    else:
        res += (v * w)
        break

print(res)