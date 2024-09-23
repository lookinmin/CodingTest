# S1, 회전초밥
from sys import stdin
import heapq
from collections import defaultdict
n, m = map(int, stdin.readline().split())

human = defaultdict(list)
for i in range(n):
    lst = list(map(int, stdin.readline().split()))[1:]
    for num in lst:
        human[num].append(i)

line = list(map(int, stdin.readline().split()))

res = [0] * n

for num in line:
    if human[num]:
        value = heapq.heappop(human[num])
        res[value] += 1
print(*res)