# 전쟁-땅따먹기
from sys import stdin
from collections import Counter

n = int(stdin.readline())
for _ in range(n):
    arr = list(map(int, stdin.readline().split()))
    soldier = arr[1:]
    count = Counter(soldier)

    if count.most_common(1)[0][1] > (arr[0] // 2):
        print(count.most_common(1)[0][0])
    else:
        print("SYJKGW")
