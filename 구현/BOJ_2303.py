from sys import stdin
from itertools import combinations

n = int(stdin.readline())
people = {}
for i in range(n):
    people[i] = list(map(int, stdin.readline().split()))

def oneNum(arr):
    k = sum(arr)
    return int(str(k)[-1])

res = {}

for i in range(n):
    maxNum = 0
    tmp = list(combinations(people[i], 3))
    for arr in tmp:
        maxNum = max(maxNum, oneNum(arr))

    res[i] = maxNum

ans = sorted(res.items(), key= lambda x : (-x[1], -x[0]))
print(ans[0][0] + 1)
