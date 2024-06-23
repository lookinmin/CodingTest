# Record Keeping, S3
from sys import stdin
from collections import defaultdict
n = int(stdin.readline())
total = defaultdict(int)
for _ in range(n):
    a, b, c = map(str, stdin.readline().split())
    total[a] += 1
    total[b] += 1
    total[c] += 1

tmp = sorted(total.items(), key = lambda x : x[1], reverse= True)
print(tmp)