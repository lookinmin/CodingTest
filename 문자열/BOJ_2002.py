# 추월, S1, 문자열, 자료구조, 해시(집합-맵)
from sys import stdin

n = int(stdin.readline())
start = dict()
end = []
res = 0
for i in range(n):
    car = stdin.readline().strip()
    start[car] = i
for _ in range(n):
    end.append(stdin.readline().strip())

print(start)

for i in range(n-1):
    for j in range(i+1, n):
        if start[end[i]] > start[end[j]]:
            res += 1
            break

print(res)