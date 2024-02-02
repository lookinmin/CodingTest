from sys import stdin
from itertools import combinations_with_replacement

n = int(stdin.readline())
nums = [1, 5, 10, 50]

res = set()

for tmp in list(combinations_with_replacement(nums, n)):
    k = 0

    for num in tmp:
        k += num

    res.add(k)

print(len(res))


