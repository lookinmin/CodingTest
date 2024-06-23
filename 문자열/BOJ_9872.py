# Record Keeping, S3
from sys import stdin
from collections import defaultdict
n = int(stdin.readline())
total = defaultdict(int)
for _ in range(n):
    lst = tuple(sorted(list(map(str, stdin.readline().split()))))
    total[lst] += 1
    

tmp = sorted(total.items(), key = lambda x : x[1], reverse= True)
print(tmp[0][1])