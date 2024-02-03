from sys import stdin
from itertools import combinations

origin = stdin.readline().rstrip()

k = len(origin)
arr = [i for i in range(1, k)]

tmp = list(combinations(arr, 2))
res = []

for seq in sorted(tmp):
    word = ''
    word += origin[:seq[0]][::-1]
    word += origin[seq[0] : seq[1]][::-1]
    word += origin[seq[1]:][::-1]
    res.append(word)
res.sort()
print(res[0])
